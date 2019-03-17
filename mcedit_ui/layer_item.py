
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

class LayerItem(QGraphicsRectItem):
  def __init__(self, room, layer_index, renderer):
    super().__init__()
    
    self.room = room
    self.layer_index = layer_index
    self.renderer = renderer
    
    try:
      self.render_layer()
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error rendering layer:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
  
  def render_layer(self):
    room = self.room
    layer_index = self.layer_index
    
    if room.area.uses_256_color_bg1s:
      if layer_index == 1:
        self.render_layer_256_color()
      else:
        # Their BG2s may be unused? They seem to error out when trying to render them. TODO figure them out
        pass
    else:
      self.render_layer_16_color()
  
  def render_layer_16_color(self):
    room = self.room
    layer_index = self.layer_index
    
    palettes = self.renderer.generate_palettes_for_area_by_gfx_index(room.area, room.gfx_index)
    tileset_image = self.renderer.render_tileset(room.area, room.gfx_index, palettes, layer_index)
    
    tile_mapping_16x16_data = room.layers_asset_list.tile_mappings[layer_index]
    if tile_mapping_16x16_data is None:
      raise Exception("Layer BG%d has no 16x16 tile mapping" % (layer_index+1))
    
    room_width_in_16x16_tiles = room.width//16
    
    cached_tile_pixmaps_by_16x16_index = {}
    for i in range(len(tile_mapping_16x16_data)//2):
      tile_map_16x16_offset = i*2
      tile_index_16x16 = tile_mapping_16x16_data.read_u16(tile_map_16x16_offset)
      
      x = (i % room_width_in_16x16_tiles)*16
      y = (i // room_width_in_16x16_tiles)*16
      
      if tile_index_16x16 in cached_tile_pixmaps_by_16x16_index:
        tile_pixmap = cached_tile_pixmaps_by_16x16_index[tile_index_16x16]
      else:
        tile_image = self.renderer.get_16x16_tile_by_index(tileset_image, tile_index_16x16)
        
        data = tile_image.tobytes('raw', 'BGRA')
        qimage = QImage(data, tile_image.size[0], tile_image.size[1], QImage.Format_ARGB32)
        tile_pixmap = QPixmap.fromImage(qimage)
        
        cached_tile_pixmaps_by_16x16_index[tile_index_16x16] = tile_pixmap
      
      tile_item = QGraphicsPixmapItem(tile_pixmap, self)
      tile_item.setPos(x, y)
  
  def render_layer_256_color(self):
    room = self.room
    layer_index = self.layer_index
    
    palettes = self.renderer.generate_palettes_for_area_by_gfx_index(room.area, room.gfx_index)
    
    layer_image = self.renderer.render_layer_256_color(self.room, palettes, layer_index)
    
    data = layer_image.tobytes('raw', 'BGRA')
    qimage = QImage(data, layer_image.size[0], layer_image.size[1], QImage.Format_ARGB32)
    layer_pixmap = QPixmap.fromImage(qimage)
    
    graphics_item = QGraphicsPixmapItem(layer_pixmap, self)
