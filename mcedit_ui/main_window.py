
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mcedit_ui.ui_main import Ui_MainWindow
from mcedit_ui.clickable_graphics_scene import *
from mcedit_ui.custom_graphics_items import *
from mcedit_ui.entity_layer_item import *
from mcedit_ui.layer_item import *
from mcedit_ui.tileset_graphics_scene import *

from mcedit_ui.entity_search_dialog import *
from mcedit_ui.save_editor_dialog import *
from mcedit_ui.text_editor_dialog import *

from mclib.game import Game
from mclib.renderer import Renderer
from mclib.docs import AREA_INDEX_TO_NAME

import os
from collections import OrderedDict
from PIL import Image
import traceback
import subprocess
import psutil

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

from paths import DATA_PATH

class MCEditorWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    
    self.open_dialogs = []
    
    self.area_index = None
    self.room_index = None
    self.area = None
    self.room = None
    
    self.layer_items = []
    self.selected_layer_index = None
    self.selected_tileset_graphics_scene = None
    self.selected_tiles_cursor = None
    
    self.last_emulator_process = None
    
    self.ui.scrollArea.setFrameShape(QFrame.NoFrame)
    
    self.room_graphics_scene = ClickableGraphicsScene()
    self.ui.room_graphics_view.setScene(self.room_graphics_scene)
    self.ui.room_graphics_view.setFocus()
    self.room_graphics_scene.clicked.connect(self.room_clicked)
    self.room_graphics_scene.clicked.connect(self.layer_clicked)
    self.room_graphics_scene.moved.connect(self.mouse_moved_on_room)
    
    self.map_graphics_scene = ClickableGraphicsScene()
    self.ui.map_graphics_view.setScene(self.map_graphics_scene)
    self.map_graphics_scene.clicked.connect(self.map_clicked)
    
    self.bg2_tileset_graphics_scene = TilesetGraphicsScene(self)
    self.ui.bg2_tileset_graphics_view.setScene(self.bg2_tileset_graphics_scene)
    self.bg1_tileset_graphics_scene = TilesetGraphicsScene(self)
    self.ui.bg1_tileset_graphics_view.setScene(self.bg1_tileset_graphics_scene)
    self.selected_tileset_graphics_scene = None
    
    self.ui.right_sidebar.currentChanged.connect(self.update_edit_mode_by_current_tab)
    QShortcut(QKeySequence(Qt.Key_F1), self, self.enter_entity_edit_mode)
    QShortcut(QKeySequence(Qt.Key_F2), self, self.enter_bg2_layer_edit_mode)
    QShortcut(QKeySequence(Qt.Key_F3), self, self.enter_bg1_layer_edit_mode)
    
    self.ui.actionOpen_ROM.triggered.connect(self.open_rom_dialog)
    
    self.ui.actionLayer_BG1.triggered.connect(self.update_visible_view_items)
    self.ui.actionLayer_BG2.triggered.connect(self.update_visible_view_items)
    self.ui.actionLayer_BG3.triggered.connect(self.update_visible_view_items)
    self.ui.actionEntities.triggered.connect(self.update_visible_view_items)
    self.ui.actionTile_Entities.triggered.connect(self.update_visible_view_items)
    self.ui.actionExits.triggered.connect(self.update_visible_view_items)
    
    self.ui.actionEntity_Search.triggered.connect(self.open_entity_search)
    self.ui.actionSave_Editor.triggered.connect(self.open_save_editor)
    self.ui.actionText_Editor.triggered.connect(self.open_text_editor)
    
    self.ui.actionTest_Room.triggered.connect(self.test_room)
    
    self.ui.area_index.activated.connect(self.area_index_changed)
    self.ui.room_index.activated.connect(self.room_index_changed)
    
    self.ui.entity_lists_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
    self.ui.entity_lists_list.itemSelectionChanged.connect(self.entity_list_visibility_toggled)
    
    #self.setWindowTitle("Minish Cap Editor %s" % VERSION)
    
    #icon_path = os.path.join(ASSETS_PATH, "icon.ico")
    #self.setWindowIcon(QIcon(icon_path))
    
    self.load_settings()
    
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
    self.close_open_dialogs()
    
    self.settings["last_used_rom"] = rom_path
    
    self.game = Game(rom_path)
    self.renderer = Renderer(self.game)
    
    self.initialize_dropdowns()
  
  def initialize_dropdowns(self):
    self.ui.area_index.clear()
    self.ui.room_index.clear()
    for area in self.game.areas:
      area_name = AREA_INDEX_TO_NAME[area.area_index]
      self.ui.area_index.addItem("%02X %s" % (area.area_index, area_name))
    
    try:
      if "last_area_index" in self.settings:
        area_index = self.settings["last_area_index"]
        room_index = self.settings["last_room_index"]
      else:
        area_index = 0
        room_index = 0
      self.area_index_changed(area_index, default_room_index=room_index)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error loading map:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
      return
  
  def area_index_changed(self, area_index, skip_loading_room=False, default_room_index=0):
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
      self.room_index_changed(default_room_index)
  
  def room_index_changed(self, room_index):
    self.save_any_unsaved_changes_for_all_layers()
    
    self.room_index = room_index
    self.ui.room_index.setCurrentIndex(room_index)
    
    if room_index >= 0 and room_index < len(self.area.rooms):
      self.room = self.area.rooms[room_index]
    else:
      self.room = None
    
    self.load_room()
    
    self.settings["last_area_index"] = self.area_index
    self.settings["last_room_index"] = self.room_index
  
  def change_area_and_room(self, area_index, room_index):
    if self.area_index != area_index:
      self.area_index_changed(area_index, skip_loading_room=True)
    
    self.room_index_changed(room_index)
  
  def change_area_and_room_by_exit(self, ext):
    self.change_area_and_room(ext.dest_area, ext.dest_room)
    dest_x = ext.dest_x
    dest_y = ext.dest_y
    if dest_x >= 0x400:
      dest_x = self.room.width/2
    if dest_y >= 0x400:
      dest_y = self.room.height/2
    self.ui.room_graphics_view.centerOn(dest_x, dest_y)
  
  def go_to_room_and_select_entity(self, entity):
    if entity.room.area.area_index != self.area.area_index or entity.room.room_index != self.room.room_index:
      self.change_area_and_room(entity.room.area.area_index, entity.room.room_index)
    self.select_entity(entity)
  
  def load_room(self):
    self.ui.entity_lists_list.clear()
    self.room_graphics_scene.clear()
    
    room_boundaries_item = QGraphicsRectItem(0, 0, self.room.width, self.room.height)
    room_boundaries_item.setBrush(QBrush(QColor(200, 200, 200, 255)))
    room_boundaries_item.setPen(QPen(QColor(255, 255, 255, 0)))
    self.room_graphics_scene.addItem(room_boundaries_item)
    
    self.selected_tiles_cursor = QGraphicsPixmapItem()
    self.selected_tiles_cursor.setZValue(99999999)
    self.room_graphics_scene.addItem(self.selected_tiles_cursor)
    self.update_selected_tiles_cursor_image()
    
    self.update_selected_room_on_map()
    
    self.center_room_view()
    
    try:
      self.renderer.update_curr_room_palettes_and_tilesets(self.room)
      
      self.bg2_tileset_graphics_scene.update_tileset_image(self.renderer.curr_room_tileset_images[2])
      self.bg1_tileset_graphics_scene.update_tileset_image(self.renderer.curr_room_tileset_images[1])
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error loading room:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
    
    if self.room is None:
      return
    
    try:
      self.load_room_layers()
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error loading room:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
    
    try:
      self.load_room_entities()
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error loading room:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
    
    self.ui.room_graphics_view.updateSceneRect(self.room_graphics_scene.itemsBoundingRect())
    
    self.update_visible_view_items()
    
    self.update_edit_mode_by_current_tab()
  
  def load_room_layers(self):
    self.layer_bg3_view_item = LayerItem(self.room, 3, self.renderer, self)
    self.room_graphics_scene.addItem(self.layer_bg3_view_item)
    self.layer_bg2_view_item = LayerItem(self.room, 2, self.renderer, self)
    self.room_graphics_scene.addItem(self.layer_bg2_view_item)
    self.layer_bg1_view_item = LayerItem(self.room, 1, self.renderer, self)
    self.room_graphics_scene.addItem(self.layer_bg1_view_item)
    
    self.layer_items = [
      None,
      self.layer_bg1_view_item,
      self.layer_bg2_view_item,
      self.layer_bg3_view_item,
    ]
  
  def load_room_entities(self):
    self.entities_view_item = EntityLayerItem(self.room.entity_lists, self.renderer)
    self.room_graphics_scene.addItem(self.entities_view_item)
    
    i = 0
    self.ui.entity_lists_list.blockSignals(True)
    for entity_list, graphics_items in self.entities_view_item.entity_graphics_items_by_entity_list:
      list_widget_item = QListWidgetItem("%02X %08X %s" % (i, entity_list.entity_list_ptr, entity_list.name))
      self.ui.entity_lists_list.addItem(list_widget_item)
      list_widget_item.setSelected(True)
      i += 1
    self.ui.entity_lists_list.blockSignals(False)
    
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
    
    for regions in self.room.exit_region_lists:
      for region in regions:
        entity_item = EntityRectItem(region, "exit_region")
        entity_item.setParentItem(self.exits_view_item)
    
    self.select_entity_graphics_item(None)
  
  def show_all_entities(self):
    self.entities_view_item.show()
    self.tile_entities_view_item.show()
    self.exits_view_item.show()
  
  def hide_all_entities(self):
    self.entities_view_item.hide()
    self.tile_entities_view_item.hide()
    self.exits_view_item.hide()
  
  def center_room_view(self):
    if self.room is not None:
      self.ui.room_graphics_view.centerOn(self.room.width/2, self.room.height/2)
  
  def room_clicked(self, x, y, button):
    graphics_item = self.room_graphics_scene.itemAt(x, y)
    if graphics_item is None:
      self.select_entity_graphics_item(None)
      return
    
    if isinstance(graphics_item, EntityRectItem) or isinstance(graphics_item, EntityImageItem):
      if button == Qt.LeftButton:
        self.select_entity_graphics_item(graphics_item)
      elif button == Qt.RightButton and graphics_item.entity_class == "exit":
        # Go through the exit into the destination room.
        self.change_area_and_room_by_exit(graphics_item.entity)
      elif button == Qt.RightButton and graphics_item.entity_class == "exit_region":
        # Go through the exit into the destination room.
        self.change_area_and_room_by_exit(graphics_item.entity.exit)
    else:
      self.select_entity_graphics_item(None)
  
  def mouse_moved_on_room(self, x, y, button):
    if button == Qt.LeftButton:
      self.layer_clicked(x, y, button)
    
    self.update_selected_tiles_cursor_position(x, y, button)
  
  
  def update_edit_mode_by_current_tab(self):
    if self.ui.right_sidebar.currentIndex() == 0:
      self.enter_entity_edit_mode()
    elif self.ui.right_sidebar.currentIndex() == 1:
      self.enter_bg2_layer_edit_mode()
    elif self.ui.right_sidebar.currentIndex() == 2:
      self.enter_bg1_layer_edit_mode()
  
  def enter_entity_edit_mode(self):
    self.ui.right_sidebar.setCurrentIndex(0)
    
    self.selected_tileset_graphics_scene = None
    self.selected_layer_index = None
    self.update_selected_tiles_cursor_image()
    self.show_all_entities()
    
    for layer_item in self.layer_items:
      if layer_item is None:
        continue
      layer_item.setOpacity(1.0)
  
  def enter_bg2_layer_edit_mode(self):
    self.enter_layer_edit_mode_by_layer_index(2)
  
  def enter_bg1_layer_edit_mode(self):
    self.enter_layer_edit_mode_by_layer_index(1)
  
  def enter_layer_edit_mode_by_layer_index(self, layer_index):
    if layer_index == 2:
      self.selected_tileset_graphics_scene = self.bg2_tileset_graphics_scene
      self.ui.right_sidebar.setCurrentIndex(1)
    elif layer_index == 1:
      self.selected_tileset_graphics_scene = self.bg1_tileset_graphics_scene
      self.ui.right_sidebar.setCurrentIndex(2)
    
    self.update_selected_tiles_cursor_image()
    
    self.selected_layer_index = layer_index
    self.hide_all_entities()
    
    for layer_item in self.layer_items:
      if layer_item is None:
        continue
      if layer_item.layer_index == layer_index:
        layer_item.setOpacity(1.0)
      else:
        layer_item.setOpacity(0.5)
  
  def update_selected_tiles_cursor_image(self):
    if self.selected_tiles_cursor is None:
      return
    
    if self.selected_tileset_graphics_scene is None:
      self.selected_tiles_cursor.hide()
    else:
      pixmap = self.selected_tileset_graphics_scene.get_selection_as_pixmap()
      self.selected_tiles_cursor.setPixmap(pixmap)
      self.selected_tiles_cursor.show()
  
  def update_selected_tiles_cursor_position(self, x, y, button):
    if self.selected_tiles_cursor is None:
      return
    
    if self.selected_tileset_graphics_scene is None:
      self.selected_tiles_cursor.hide()
    elif x < 0 or y < 0 or x >= self.room.width or y >= self.room.height:
      self.selected_tiles_cursor.hide()
    else:
      self.selected_tiles_cursor.setPos(x//0x10*0x10, y//0x10*0x10)
      self.selected_tiles_cursor.show()
  
  def layer_clicked(self, x, y, button):
    if self.selected_layer_index is not None:
      layer_item = self.layer_items[self.selected_layer_index]
      layer_item.layer_clicked(x, y, button)
      return
  
  def save_any_unsaved_changes_for_all_layers(self):
    if self.room is None:
      return
    
    try:
      for layer_index in range(4):
        print(layer_index)
        layer = self.room.layers_asset_list.layers[layer_index]
        if layer is not None:
          layer.save_any_unsaved_changes()
    except Exception as e:
      QMessageBox.warning(self,
        "Error saving layer changes",
        str(e)
      )
  
  
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
    
    self.selected_room_graphics_item = QGraphicsRectItem()
    self.selected_room_graphics_item.setPen(QPen(QColor(220, 0, 0, 255)))
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
          and not area.area_index in [0x5F, 0x71, 0x77]
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
    
    old_rect = self.selected_room_graphics_item.rect()
    
    if self.room is None:
      x = 0
      y = 0
      w = 0
      h = 0
    elif self.area.is_overworld:
      x = self.room.x_pos/0x19
      y = self.room.y_pos/0x19
      w = self.room.width/0x19-1
      h = self.room.height/0x19-1
    else:
      x = self.room.x_pos/0x10
      y = self.room.y_pos/0x10
      w = self.room.width/0x10-1
      h = self.room.height/0x10-1
    
    self.selected_room_graphics_item.setRect(
      x, y, w, h
    )
    
    self.map_graphics_scene.setSceneRect(self.map_graphics_scene.itemsBoundingRect())
    
    if w != 0:
      center_x = x + w/2
      center_y = y + h/2
      self.ui.map_graphics_view.centerOn(center_x, center_y)
      self.map_graphics_scene.invalidate(old_rect)
  
  def update_visible_view_items(self):
    self.layer_bg1_view_item.setVisible(self.ui.actionLayer_BG1.isChecked())
    self.layer_bg2_view_item.setVisible(self.ui.actionLayer_BG2.isChecked())
    self.layer_bg3_view_item.setVisible(self.ui.actionLayer_BG3.isChecked())
    self.entities_view_item.setVisible(self.ui.actionEntities.isChecked())
    self.tile_entities_view_item.setVisible(self.ui.actionTile_Entities.isChecked())
    self.exits_view_item.setVisible(self.ui.actionExits.isChecked())
  
  def entity_list_visibility_toggled(self):
    for entity_list_index in range(self.ui.entity_lists_list.count()):
      list_widget_item = self.ui.entity_lists_list.item(entity_list_index)
      entity_list, graphics_items = self.entities_view_item.entity_graphics_items_by_entity_list[entity_list_index]
      for entity_item in graphics_items:
        entity_item.setVisible(list_widget_item.isSelected())
  
  def select_entity_graphics_item(self, entity_graphics_item):
    if entity_graphics_item:
      for other_entity_graphics_item in self.entities_view_item.childItems():
        other_entity_graphics_item.setSelected(False)
      
      entity_graphics_item.setSelected(True)
    
    self.ui.entity_properies.select_entity_graphics_item(entity_graphics_item)
  
  def select_entity(self, entity):
    entity_graphics_item = next((
      egi for egi in self.entities_view_item.childItems()
      if egi.entity == entity
    ), None)
    if entity_graphics_item is None:
      return
    self.select_entity_graphics_item(entity_graphics_item)
    self.ui.room_graphics_view.centerOn(entity_graphics_item)
  
  
  def close_open_dialogs(self):
    for dialog in self.open_dialogs:
      dialog.close()
    self.open_dialogs = []
  
  def open_entity_search(self):
    entity_search_dialog = EntitySearchDialog(self)
    self.open_dialogs.append(entity_search_dialog)
  
  def open_save_editor(self):
    dialog = SaveEditorDialog(self)
    self.open_dialogs.append(dialog)
  
  def open_text_editor(self):
    dialog = TextEditorDialog(self)
    self.open_dialogs.append(dialog)
  
  
  def test_room(self):
    # TODO: add settings window to set the emulator path
    if self.settings.get("emulator_path") is None:
      QMessageBox.warning(self,
        "Emulator path not set",
        "Must set emulator path in the settings before running test room."
      )
      return
    emulator_path = self.settings["emulator_path"]
    
    self.save_any_unsaved_changes_for_all_layers()
    
    # Kill the last running emulator process if the user didn't do it manually.
    if self.last_emulator_process is not None:
      if self.last_emulator_process.is_running():
        self.last_emulator_process.kill()
      self.last_emulator_process = None
    
    # Apply the test room patch and set where to load the player at.
    scene_pos = self.ui.room_graphics_view.mapToScene(self.ui.room_graphics_view.mapFromGlobal(QCursor.pos()))
    test_rom = self.game.rom.copy()
    self.game.apply_patch("test_room", rom=test_rom)
    sym = self.game.custom_symbols["test_room_data"]
    test_rom.write_u8(sym, self.area_index)
    test_rom.write_u8(sym+1, self.room_index)
    test_rom.write_u16(sym+2, scene_pos.x())
    test_rom.write_u16(sym+4, scene_pos.y())
    
    # Write the test ROM.
    input_rom_path = self.settings["last_used_rom"]
    output_dir = os.path.dirname(input_rom_path)
    input_rom_basename, file_ext = os.path.splitext(os.path.basename(input_rom_path))
    output_rom_basename = input_rom_basename + " Test"
    output_rom_path = os.path.join(output_dir, output_rom_basename + ".gba")
    output_rom_path = os.path.abspath(output_rom_path)
    output_rom_path = output_rom_path.replace("/", "\\")
    with open(output_rom_path, "wb") as f:
      f.write(test_rom.read_all_bytes())
    
    # Copy the symbol map file to be next to the test room ROM so that No$GBA can load it.
    input_map_path = os.path.join(DATA_PATH, "symbol_map.sym")
    with open(input_map_path) as f:
      symbol_map = f.read()
    output_map_path = os.path.join(output_dir, output_rom_basename + ".sym")
    with open(output_map_path, "w") as f:
      f.write(symbol_map)
    
    # Launch the emulator.
    popen_process = subprocess.Popen([emulator_path, output_rom_path])
    self.last_emulator_process = psutil.Process(popen_process.pid)
  
  
  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
      self.close()
  
  def closeEvent(self, event):
    #cancelled = self.confirm_discard_changes()
    #if cancelled:
    #  event.ignore()
    #  return
    
    for dialog in self.open_dialogs:
      dialog.close()
    
    self.save_settings()
