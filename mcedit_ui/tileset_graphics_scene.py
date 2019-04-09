
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mcedit_ui.clickable_graphics_scene import ClickableGraphicsScene
from mcedit_ui.custom_graphics_items import GraphicsImageItem

class TilesetGraphicsScene(ClickableGraphicsScene):
  def __init__(self):
    super().__init__()
    
    self.selected_tile_index = 0
    
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
    
    tile_index_16x16 = (y//0x10)*0x10 + (x//0x10)
    self.selected_tile_index = tile_index_16x16
    
    self.update_selection_rect()
  
  def update_tileset_image(self, new_image):
    self.tileset_graphics_item.set_image(new_image)
  
  def update_selection_rect(self):
    tile_x = self.selected_tile_index % 0x10
    tile_y = self.selected_tile_index // 0x10
    self.selection_rect.setPos(tile_x*0x10, tile_y*0x10)
    self.selection_rect.setRect(0, 0, 16, 16)
    
    if len(self.views()) > 0:
      self.views()[0].ensureVisible(self.selection_rect, xmargin=0, ymargin=0)
