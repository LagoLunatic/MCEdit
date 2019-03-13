
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class GraphicsImageItem(QGraphicsPixmapItem):
  def __init__(self, pil_image):
    width, height = pil_image.size
    
    data = pil_image.tobytes('raw', 'BGRA')
    qimage = QImage(data, width, height, QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qimage)
    super().__init__(pixmap)
    
    self.setOffset(-width//2, -height//2)

class EntityImageItem(GraphicsImageItem):
  def __init__(self, image, entity, entity_class):
    super().__init__(image)
    
    self.entity = entity
    self.entity_class = entity_class
    
    self.setFlag(QGraphicsItem.ItemIsMovable)
    #self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
    
    self.setCursor(QCursor(Qt.SizeAllCursor))
    
    if entity_class == "tile_entity":
      self.setPos(entity.x_pos*16+8, entity.y_pos*16+8)
    else:
      self.setPos(entity.x_pos, entity.y_pos)

class EntityRectItem(QGraphicsRectItem):
  ENTITY_BRUSH = QBrush(QColor(200, 0, 200, 150))
  TILE_ENTITY_BRUSH = QBrush(QColor(0, 0, 200, 150))
  EXIT_BRUSH = QBrush(QColor(200, 200, 200, 150))
  ENEMY_BRUSH = QBrush(QColor(200, 0, 0, 150))
  
  def __init__(self, entity, entity_class):
    super().__init__(-8, -8, 16, 16)
    
    self.entity = entity
    self.entity_class = entity_class
    
    self.setFlag(QGraphicsItem.ItemIsMovable)
    #self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
    
    self.setCursor(QCursor(Qt.SizeAllCursor))
    
    if entity_class == "tile_entity":
      self.setPos(entity.x_pos*16+8, entity.y_pos*16+8)
    else:
      self.setPos(entity.x_pos, entity.y_pos)
    
    if entity_class == "entity":
      if entity.type == 3:
        self.setBrush(self.ENEMY_BRUSH)
      else:
        self.setBrush(self.ENTITY_BRUSH)
    elif entity_class == "tile_entity":
      self.setBrush(self.TILE_ENTITY_BRUSH)
    elif entity_class == "exit":
      self.setBrush(self.EXIT_BRUSH)
