
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mcedit_ui.clickable_graphics_scene import ClickableGraphicsScene
from mcedit_ui.custom_graphics_items import GraphicsImageItem

class TilesetGraphicsScene(ClickableGraphicsScene):
  def __init__(self, main_window):
    super().__init__()
    
    self.main_window = main_window
    
    self.selected_tile_indexes = [0]
    self.selection_x = 0
    self.selection_y = 0
    self.selection_w = 1
    self.selection_h = 1
    self.selection_origin = None
    
    self.clicked.connect(self.mouse_clicked_on_tileset)
    self.moved.connect(self.mouse_moved_on_tileset)
    self.released.connect(self.mouse_released_on_tileset)
    
    self.tileset_graphics_item = GraphicsImageItem()
    self.addItem(self.tileset_graphics_item)
    
    self.selection_rect = QGraphicsRectItem()
    self.selection_rect.setPen(QPen(QColor(255, 0, 0, 255)))
    self.addItem(self.selection_rect)
    self.update_selection_rect()
  
  def mouse_clicked_on_tileset(self, x, y, button):
    if x < 0 or y < 0 or x >= self.tileset_width or y >= self.tileset_height:
      return
    if button != Qt.LeftButton:
      return
    
    self.selection_origin = QPoint(x//0x10, y//0x10)
    self.update_selection_on_tileset(x, y)
  
  def mouse_moved_on_tileset(self, x, y, button):
    if button != Qt.LeftButton:
      return
    
    self.update_selection_on_tileset(x, y)
  
  def mouse_released_on_tileset(self, x, y, button):
    if button != Qt.LeftButton:
      return
    
    self.update_selection_on_tileset(x, y)
    self.stop_selecting_on_tileset()
  
  def update_selection_on_tileset(self, mouse_x, mouse_y):
    mouse_x = max(mouse_x, 0)
    mouse_y = max(mouse_y, 0)
    mouse_x = min(mouse_x, self.tileset_width-1)
    mouse_y = min(mouse_y, self.tileset_height-1)
    mouse_x = mouse_x//0x10
    mouse_y = mouse_y//0x10
    
    self.selection_x = min(mouse_x, self.selection_origin.x())
    self.selection_y = min(mouse_y, self.selection_origin.y())
    selection_right_x = max(mouse_x, self.selection_origin.x())
    selection_bottom_y = max(mouse_y, self.selection_origin.y())
    self.selection_w = selection_right_x - self.selection_x + 1
    self.selection_h = selection_bottom_y - self.selection_y + 1
    
    self.update_selection_rect()
    
    self.selected_tile_indexes = []
    for y in range(self.selection_y, self.selection_y+self.selection_h):
      for x in range(self.selection_x, self.selection_x+self.selection_w):
        tile_index = x + y*0x10
        self.selected_tile_indexes.append(tile_index)
  
  def stop_selecting_on_tileset(self):
    self.selection_origin = None
    
    self.main_window.update_selected_tiles_cursor_image()
  
  def select_tile_by_index(self, tile_index_16x16):
    self.selected_tile_indexes = [tile_index_16x16]
    self.selection_x = tile_index_16x16 % 0x10
    self.selection_y = tile_index_16x16 // 0x10
    self.selection_w = 1
    self.selection_h = 1
    self.update_selection_rect()
    
    self.main_window.update_selected_tiles_cursor_image()
  
  def select_tile_by_pos(self, x, y):
    tile_index_16x16 = (y//0x10)*0x10 + (x//0x10)
    self.select_tile_by_index(tile_index_16x16)
  
  def update_tileset_image(self, new_image):
    self.tileset_graphics_item.set_image(new_image)
    self.tileset_width = new_image.width
    self.tileset_height = new_image.height
  
  def update_selection_rect(self):
    self.selection_rect.setPos(self.selection_x*0x10, self.selection_y*0x10)
    self.selection_rect.setRect(0, 0, self.selection_w*0x10, self.selection_h*0x10)
    
    if len(self.views()) > 0:
      self.views()[0].ensureVisible(self.selection_rect, xmargin=0, ymargin=0)
  
  def get_selection_as_pixmap(self):
    return self.tileset_graphics_item.pixmap().copy(
      self.selection_x*0x10, self.selection_y*0x10,
      self.selection_w*0x10, self.selection_h*0x10
    )
