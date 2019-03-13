
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
  
  def boundingRect(self):
    # If the sprite is smaller than 16x16, make sure the bounding rectangle is at least 16x16.
    
    orig_rect = super().boundingRect()
    top = orig_rect.top()
    bottom = orig_rect.bottom()
    left = orig_rect.left()
    right = orig_rect.right()
    
    if top > -8:
      top = -8
    if bottom < 8:
      bottom = 8
    if left > -8:
      left = -8
    if right < 8:
      right = 8
    
    return QRectF(left, top, right-left, bottom-top)
  
  def shape(self):
    # Make the whole bounding rectangle clickable, instead of just the sprite's pixels.
    path = QPainterPath()
    path.addRect(self.boundingRect())
    return path
  
  def paint(self, painter, option, widget):
    # Draw a border around the sprite.
    pen = painter.pen()
    rect = self.boundingRect()
    painter.drawRect(QRect(rect.x(), rect.y(), rect.width()-pen.width(), rect.height()-pen.width()))
    
    super().paint(painter, option, widget)

class EntityImageItem(GraphicsImageItem):
  def __init__(self, image, entity, entity_class):
    super().__init__(image)
    
    self.entity = entity
    self.entity_class = entity_class
    
    self.setFlag(QGraphicsItem.ItemIsMovable)
    #self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
    self.setFlag(QGraphicsItem.ItemIsSelectable)
    
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
