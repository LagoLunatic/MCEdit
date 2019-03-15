
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mcedit_ui.ui_main import Ui_MainWindow
from mcedit_ui.clickable_graphics_scene import *
from mcedit_ui.custom_graphics_items import *
from mcedit_ui.entity_layer_item import *

from mclib.game import Game
from mclib.renderer import Renderer

import os
from collections import OrderedDict
from PIL import Image
import traceback

import yaml
try:
  from yaml import CDumper as Dumper
except ImportError:
  from yaml import Dumper

# Allow yaml to load and dump OrderedDicts.
yaml.SafeLoader.add_constructor(
  yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
  lambda loader, node: OrderedDict(loader.construct_pairs(node))
)
yaml.Dumper.add_representer(
  OrderedDict,
  lambda dumper, data: dumper.represent_dict(data.items())
)

class MCEditorWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    
    self.room_graphics_scene = ClickableGraphicsScene()
    self.ui.room_graphics_view.setScene(self.room_graphics_scene)
    self.ui.room_graphics_view.setFocus()
    self.room_graphics_scene.clicked.connect(self.room_clicked)
    
    self.map_graphics_scene = ClickableGraphicsScene()
    self.ui.map_graphics_view.setScene(self.map_graphics_scene)
    self.map_graphics_scene.clicked.connect(self.map_clicked)
    
    self.load_settings()
    
    self.ui.actionOpen_ROM.triggered.connect(self.open_rom_dialog)
    
    self.ui.actionLayer_BG1.triggered.connect(self.update_visible_view_items)
    self.ui.actionLayer_BG2.triggered.connect(self.update_visible_view_items)
    self.ui.actionEntities.triggered.connect(self.update_visible_view_items)
    self.ui.actionTile_Entities.triggered.connect(self.update_visible_view_items)
    self.ui.actionExits.triggered.connect(self.update_visible_view_items)
    
    self.ui.area_index.activated.connect(self.area_index_changed)
    self.ui.room_index.activated.connect(self.room_index_changed)
    
    self.ui.entity_lists_list.itemChanged.connect(self.entity_list_visibility_toggled)
    
    #self.setWindowTitle("Minish Cap Editor %s" % VERSION)
    
    #icon_path = os.path.join(ASSETS_PATH, "icon.ico")
    #self.setWindowIcon(QIcon(icon_path))
    
    self.setWindowState(Qt.WindowMaximized)
    
    self.show()
    
    if "last_used_rom" in self.settings and os.path.isfile(self.settings["last_used_rom"]):
      self.open_rom(self.settings["last_used_rom"])
  
  def load_settings(self):
    self.settings_path = "settings.txt"
    if os.path.isfile(self.settings_path):
      with open(self.settings_path) as f:
        self.settings = yaml.safe_load(f)
      if self.settings is None:
        self.settings = OrderedDict()
    else:
      self.settings = OrderedDict()
  
  def save_settings(self):
    with open(self.settings_path, "w") as f:
      yaml.dump(self.settings, f, default_flow_style=False, Dumper=yaml.Dumper)
  
  def open_rom_dialog(self):
    default_dir = None
    
    rom_path, selected_filter = QFileDialog.getOpenFileName(self, "Select Minish Cap ROM to open", default_dir, "GBA ROM Files (*.gba)")
    if not rom_path:
      return
    
    self.open_rom(rom_path)
  
  def open_rom(self, rom_path):
    self.settings["last_used_rom"] = rom_path
    
    self.game = Game(rom_path)
    self.renderer = Renderer(self.game)
    
    self.initialize_dropdowns()
  
  def initialize_dropdowns(self):
    self.ui.area_index.clear()
    self.ui.room_index.clear()
    for area in self.game.areas:
      area_name = self.game.area_index_to_name[area.area_index]
      self.ui.area_index.addItem("%02X %s" % (area.area_index, area_name))
    self.area_index_changed(0)
  
  def area_index_changed(self, area_index, skip_loading_room=False):
    self.area_index = area_index
    self.ui.area_index.setCurrentIndex(area_index)
    self.ui.room_index.clear()
    
    self.area = self.game.areas[self.area_index]
    
    for room_index, room in enumerate(self.area.rooms):
      if room is None:
        room_text = "%02X INVALID" % room_index
      else:
        room_text = "%02X %08X %08X" % (room.room_index, room.gfx_metadata_ptr, room.property_list_ptr)
      self.ui.room_index.addItem(room_text)
    
    try:
      self.load_map()
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error loading map:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
      return
    
    if not skip_loading_room:
      self.room_index_changed(0)
  
  def room_index_changed(self, room_index):
    self.room_index = room_index
    self.ui.room_index.setCurrentIndex(room_index)
    
    if room_index >= 0 and room_index < len(self.area.rooms):
      self.room = self.area.rooms[room_index]
      self.room_bg_palettes = self.renderer.generate_palettes_for_area_by_gfx_index(self.area, self.room.gfx_index)
    else:
      self.room = None
      self.room_bg_palettes = None
    
    self.load_room()
  
  def change_area_and_room(self, area_index, room_index):
    if self.area_index != area_index:
      self.area_index_changed(area_index, skip_loading_room=True)
    
    self.room_index_changed(room_index)
  
  def load_room(self):
    self.room_graphics_scene.clear()
    self.ui.entity_lists_list.clear()
    
    self.update_selected_room_on_map()
    
    if self.room is None:
      return
    
    self.load_room_layers()
    
    self.load_room_entities()
    
    self.room_graphics_scene.setSceneRect(self.room_graphics_scene.itemsBoundingRect())
    
    self.update_visible_view_items()
  
  def load_room_layers(self):
    self.layer_bg2_view_item = QGraphicsPixmapItem()
    self.room_graphics_scene.addItem(self.layer_bg2_view_item)
    self.layer_bg1_view_item = QGraphicsPixmapItem()
    self.room_graphics_scene.addItem(self.layer_bg1_view_item)
    layer_bg_view_items = [
      self.layer_bg2_view_item,
      self.layer_bg1_view_item,
    ]
    
    try:
      for layer_index in range(2):
        layer_image = self.renderer.render_layer(self.room, self.room_bg_palettes, layer_index)
        
        data = layer_image.tobytes('raw', 'BGRA')
        qimage = QImage(data, layer_image.size[0], layer_image.size[1], QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(qimage)
        
        layer_bg_view_item = layer_bg_view_items[layer_index]
        layer_bg_view_item.setPixmap(pixmap)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error rendering room:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
  
  def load_room_entities(self):
    self.entities_view_item = EntityLayerItem(self.room.entity_lists, self.renderer, self.room_bg_palettes)
    self.room_graphics_scene.addItem(self.entities_view_item)
    
    i = 0
    for entity_list, graphics_items in self.entities_view_item.entity_graphics_items_by_entity_list:
      list_widget_item = QListWidgetItem("%02X %08X %s" % (i, entity_list.entity_list_ptr, entity_list.name))
      list_widget_item.setFlags(list_widget_item.flags() | Qt.ItemIsUserCheckable)
      list_widget_item.setCheckState(Qt.Checked)
      self.ui.entity_lists_list.addItem(list_widget_item)
      i += 1
    
    self.tile_entities_view_item = QGraphicsRectItem()
    self.room_graphics_scene.addItem(self.tile_entities_view_item)
    for tile_entity in self.room.tile_entities:
      entity_item = EntityRectItem(tile_entity, "tile_entity")
      entity_item.setParentItem(self.tile_entities_view_item)
    
    self.exits_view_item = QGraphicsRectItem()
    self.room_graphics_scene.addItem(self.exits_view_item)
    for ext in self.room.exits:
      entity_item = EntityRectItem(ext, "exit")
      entity_item.setParentItem(self.exits_view_item)
    
    self.select_entity(None)
  
  def room_clicked(self, x, y, button):
    graphics_item = self.room_graphics_scene.itemAt(x, y)
    if graphics_item is None:
      self.select_entity(None)
      return
    
    if isinstance(graphics_item, EntityRectItem) or isinstance(graphics_item, EntityImageItem):
      if button == Qt.LeftButton:
        self.select_entity(graphics_item)
      elif button == Qt.RightButton and graphics_item.entity_class == "exit":
        # Go through the exit into the destination room.
        self.change_area_and_room(graphics_item.entity.dest_area, graphics_item.entity.dest_room)
    else:
      self.select_entity(None)
  
  def load_map(self):
    self.map_graphics_scene.clear()
    
    self.selected_room_graphics_item = None
    
    if self.area.is_dungeon:
      dungeon = self.game.dungeons[self.area.dungeon_index]
      map_image = self.renderer.render_dungeon_map(dungeon)
    elif self.area.is_overworld:
      map_image = self.renderer.render_world_map()
    else:
      map_image = self.renderer.render_dummy_map(self.area)
    
    data = map_image.tobytes('raw', 'BGRA')
    qimage = QImage(data, map_image.size[0], map_image.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qimage)
    
    map_graphics_item = QGraphicsPixmapItem(pixmap)
    self.map_graphics_scene.addItem(map_graphics_item)
    
    #self.ui.map_graphics_view.resize(map_image.size[0]+4, map_image.size[1]+4)
    
    self.selected_room_graphics_item = QGraphicsRectItem()
    self.selected_room_graphics_item.setRect(0, 0, 0, 0)
    self.map_graphics_scene.addItem(self.selected_room_graphics_item)
    
    self.map_graphics_scene.setSceneRect(self.map_graphics_scene.itemsBoundingRect())
  
  def map_clicked(self, x, y, button):
    if button == Qt.LeftButton:
      if self.area.is_overworld:
        areas_to_check = [
          area for area in self.game.areas
          if area.is_overworld
          and not area.area_index in [0x15]
        ]
      elif self.area.is_dungeon:
        areas_to_check = [
          area for area in self.game.areas
          if area.is_dungeon and area.dungeon_index == self.area.dungeon_index
        ]
      else:
        areas_to_check = [self.area]
      
      for area in areas_to_check:
        for room in area.rooms:
          if room is None:
            continue
          
          if self.area.is_overworld:
            room_x = room.x_pos  / 0x19
            room_y = room.y_pos  / 0x19
            room_w = room.width  / 0x19
            room_h = room.height / 0x19
          else:
            room_x = room.x_pos  / 0x10
            room_y = room.y_pos  / 0x10
            room_w = room.width  / 0x10
            room_h = room.height / 0x10
          
          if x >= room_x and y >= room_y and x < room_x+room_w and y < room_y+room_h:
            # Go into the clicked room.
            self.change_area_and_room(area.area_index, room.room_index)
            break
  
  def update_selected_room_on_map(self):
    if self.selected_room_graphics_item is None:
      return
    
    if self.room is None:
      self.selected_room_graphics_item.setRect(
        0, 0, 0, 0
      )
    elif self.area.is_overworld:
      self.selected_room_graphics_item.setRect(
        self.room.x_pos/0x19, self.room.y_pos/0x19, self.room.width/0x19-1, self.room.height/0x19-1
      )
    else:
      self.selected_room_graphics_item.setRect(
        self.room.x_pos/0x10, self.room.y_pos/0x10, self.room.width/0x10-1, self.room.height/0x10-1
      )
    
    self.map_graphics_scene.setSceneRect(self.map_graphics_scene.itemsBoundingRect())
  
  def update_visible_view_items(self):
    self.layer_bg1_view_item.setVisible(self.ui.actionLayer_BG1.isChecked())
    self.layer_bg2_view_item.setVisible(self.ui.actionLayer_BG2.isChecked())
    self.entities_view_item.setVisible(self.ui.actionEntities.isChecked())
    self.tile_entities_view_item.setVisible(self.ui.actionTile_Entities.isChecked())
    self.exits_view_item.setVisible(self.ui.actionExits.isChecked())
  
  def entity_list_visibility_toggled(self, list_widget_item):
    entity_list_index = int(list_widget_item.text().split(" ")[0], 16)
    entity_list, graphics_items = self.entities_view_item.entity_graphics_items_by_entity_list[entity_list_index]
    
    for entity_item in graphics_items:
      entity_item.setVisible(list_widget_item.checkState() == Qt.Checked)
  
  def select_entity(self, entity_graphics_item):
    self.ui.entity_properies.select_entity(entity_graphics_item)
  
  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
      self.close()
  
  def closeEvent(self, event):
    #cancelled = self.confirm_discard_changes()
    #if cancelled:
    #  event.ignore()
    #  return
    
    self.save_settings()
