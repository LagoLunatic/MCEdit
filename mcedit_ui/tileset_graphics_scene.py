
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
    
    self.clicked.connect(self.tileset_clicked)
    
    self.tileset_graphics_item = GraphicsImageItem()
    self.addItem(self.tileset_graphics_item)
    
    self.selection_rect = QGraphicsRectItem()
    self.selection_rect.setPen(QPen(QColor(255, 0, 0, 255)))
    self.addItem(self.selection_rect)
    self.update_selection_rect()
  
  def tileset_clicked(self, x, y, button):
    tileset_width = self.tileset_graphics_item.pixmap().width()
    tileset_height = self.tileset_graphics_item.pixmap().height()
    if x < 0 or y < 0 or x >= tileset_width or y >= tileset_height:
      return
    if button != Qt.LeftButton:
      return
    
    self.select_tile_by_pos(x, y)
  
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
