
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

from mclib.visual_zone import VisualZone

class LayerItem(QGraphicsRectItem):
  def __init__(self, room, layer_index, renderer):
    super().__init__()
    
    self.room = room
    self.layer_index = layer_index
    self.renderer = renderer
    self.rom = room.rom
    
    try:
      self.render_layer()
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error rendering layer in room %02X-%02X:\n" % (room.area.area_index, room.room_index)
      error_message += str(e) + "\n\n" + stack_trace
      print(error_message)
  
  def render_layer(self):
    room = self.room
    area = room.area
    layer_index = self.layer_index
    
    if room.area.uses_256_color_bg1s:
      if layer_index == 2:
        self.render_layer_mapped(color_mode=256)
      else:
        # Their BG1s may be unused? They seem to error out when trying to render them. TODO figure them out
        pass
    else:
      if layer_index == 3:
        if area.get_gfx_asset_list(room.gfx_index).tile_mappings_8x8[layer_index] is None:
          return
        self.render_layer_mapped(color_mode=16)
      elif room.layers_asset_list.tile_mappings_8x8[layer_index] is not None:
        self.render_layer_mapped(color_mode=16)
      else:
        self.render_layer_16_color()
  
  def render_layer_16_color(self):
    room = self.room
    area = room.area
    layer_index = self.layer_index
    
    gfx_asset_list = area.get_gfx_asset_list(room.gfx_index)
    orig_gfx_data = gfx_asset_list.gfx_data
    if layer_index in [1, 3]:
      self.gfx_data = orig_gfx_data.read_raw(0x4000, len(orig_gfx_data)-0x4000)
    else:
      self.gfx_data = orig_gfx_data
    self.palettes = self.renderer.generate_palettes_for_area_by_gfx_index(room.area, room.gfx_index)
    self.tileset_data = room.area.tilesets_asset_list.tileset_datas[layer_index]
    if self.tileset_data is None:
      return
    
    layer_data = room.layers_asset_list.layer_datas[layer_index]
    if layer_data is None:
      raise Exception("Layer BG%d has no layer data" % layer_index)
    if len(layer_data) == 0:
      raise Exception("Layer BG%d has zero-length layer data" % layer_index)
    if layer_data[0] == 0xFFFF:
      # No real layer data here
      return
    
    self.cached_8x8_tile_images_by_tile_attrs_and_zone_ids = {}
    
    room_width_in_16x16_tiles = room.width//16
    
    cached_tile_pixmaps_by_16x16_index = {}
    for i in range(len(layer_data)):
      tile_index_16x16 = self.layer_data[i]
      
      x = (i % room_width_in_16x16_tiles)*16
      y = (i // room_width_in_16x16_tiles)*16
      
      if tile_index_16x16 in cached_tile_pixmaps_by_16x16_index:
        tile_pixmap = cached_tile_pixmaps_by_16x16_index[tile_index_16x16]
      else:
        tile_pixmap = self.render_tile_pixmap_by_16x16_tile_index(tile_index_16x16, x, y)
        
        cached_tile_pixmaps_by_16x16_index[tile_index_16x16] = tile_pixmap
      
      tile_item = QGraphicsPixmapItem(tile_pixmap, self)
      tile_item.setPos(x, y)
  
  def render_tile_pixmap_by_16x16_tile_index(self, tile_index_16x16, x, y):
    room = self.room
    layer_index = self.layer_index
    gfx_data = self.gfx_data
    palettes = self.palettes
    zone_ids = []
    
    if self.room.zone_lists:
      zone_ids = VisualZone.get_zone_ids_overlapping_point(self.room.zone_lists, x, y)
      
      if zone_ids:
        gfx_data = gfx_data.copy()
      
      for zone_id in zone_ids:
        zone_data = room.visual_zone_datas[zone_id]
        
        if zone_data.palette_group_index is not None:
          palettes = self.renderer.generate_palettes_from_palette_group_by_index(zone_data.palette_group_index)
        
        for zone_gfx_data_ptr, zone_gfx_load_offset in zone_data.gfx_load_datas:
          if layer_index in [1, 3]:
            zone_gfx_load_offset -= 0x4000
            if zone_gfx_load_offset < 0:
              continue
          
          zone_gfx_data = self.rom.read_raw(zone_gfx_data_ptr, 0x1000)
          gfx_data.write_raw(zone_gfx_load_offset, zone_gfx_data)
    
    tile_image_16x16 = QImage(16, 16, QImage.Format_ARGB32)
    tile_image_16x16.fill(0)
    painter = QPainter(tile_image_16x16)
    
    zone_ids_tuple = tuple(zone_ids)
    if zone_ids_tuple not in self.cached_8x8_tile_images_by_tile_attrs_and_zone_ids:
      self.cached_8x8_tile_images_by_tile_attrs_and_zone_ids[zone_ids_tuple] = {}
    cached_8x8_tile_images_by_tile_attrs = self.cached_8x8_tile_images_by_tile_attrs_and_zone_ids[zone_ids_tuple]
    
    try:
      for tile_8x8_i in range(4):
        tile_attrs = self.tileset_data[tile_index_16x16*4 + tile_8x8_i]
        
        horizontal_flip = (tile_attrs & 0x0400) > 0
        vertical_flip   = (tile_attrs & 0x0800) > 0
        
        # Remove flip bits so all 4 orientations can be cached together as one.
        tile_attrs &= (~0x0C00)
        
        if tile_attrs in cached_8x8_tile_images_by_tile_attrs:
          tile_image_8x8 = cached_8x8_tile_images_by_tile_attrs[tile_attrs]
        else:
          pil_image = self.renderer.render_tile_by_tile_attrs(tile_attrs, gfx_data, palettes)
          data = pil_image.tobytes('raw', 'BGRA')
          tile_image_8x8 = QImage(data, pil_image.size[0], pil_image.size[1], QImage.Format_ARGB32)
          cached_8x8_tile_images_by_tile_attrs[tile_attrs] = tile_image_8x8
        
        if horizontal_flip and vertical_flip:
          tile_image_8x8 = tile_image_8x8.transformed(QTransform.fromScale(-1, -1))
        elif horizontal_flip:
          tile_image_8x8 = tile_image_8x8.transformed(QTransform.fromScale(-1, 1))
        elif vertical_flip:
          tile_image_8x8 = tile_image_8x8.transformed(QTransform.fromScale(1, -1))
        
        x_on_16x16_tile = (tile_8x8_i % 2)*8
        y_on_16x16_tile = (tile_8x8_i // 2)*8
        
        painter.drawImage(x_on_16x16_tile, y_on_16x16_tile, tile_image_8x8)
    except:
      # Need to properly end the painter or the program will crash
      painter.end()
      raise
    
    painter.end()
    
    tile_pixmap = QPixmap.fromImage(tile_image_16x16)
    
    return tile_pixmap
  
  def render_layer_mapped(self, color_mode=256):
    room = self.room
    layer_index = self.layer_index
    
    palettes = self.renderer.generate_palettes_for_area_by_gfx_index(room.area, room.gfx_index)
    
    layer_image = self.renderer.render_layer_mapped(self.room, palettes, layer_index, color_mode=color_mode)
    
    data = layer_image.tobytes('raw', 'BGRA')
    qimage = QImage(data, layer_image.size[0], layer_image.size[1], QImage.Format_ARGB32)
    layer_pixmap = QPixmap.fromImage(qimage)
    
    graphics_item = QGraphicsPixmapItem(layer_pixmap, self)
