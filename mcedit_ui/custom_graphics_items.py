
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class GraphicsImageItem(QGraphicsPixmapItem):
  def __init__(self, pil_image=None):
    super().__init__()
    
    self.set_image(pil_image)
  
  def set_image(self, pil_image):
    if pil_image is None:
      width = 16
      height = 16
      pixmap = QPixmap(width, height)
      pixmap.fill(QColor(200, 0, 200, 150))
      self.setPixmap(pixmap)
    else:
      width, height = pil_image.size
      
      data = pil_image.tobytes('raw', 'BGRA')
      qimage = QImage(data, width, height, QImage.Format_ARGB32)
      pixmap = QPixmap.fromImage(qimage)
      self.setPixmap(pixmap)
    
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
  def __init__(self, entity, entity_class, renderer):
    super().__init__()
    
    self.entity = entity
    self.entity_class = entity_class
    self.renderer = renderer
    
    self.setFlag(QGraphicsItem.ItemIsMovable)
    #self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
    self.setFlag(QGraphicsItem.ItemIsSelectable)
    
    self.setCursor(QCursor(Qt.SizeAllCursor))
    
    self.update_from_entity()
  
  def update_from_entity(self):
    image = self.renderer.render_entity_sprite_frame(self.entity)
    self.set_image(image)
    
    if self.entity_class == "tile_entity":
      self.setPos(self.entity.x_pos*16+8, self.entity.y_pos*16+8)
    else:
      self.setPos(self.entity.x_pos, self.entity.y_pos)

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
    self.setFlag(QGraphicsItem.ItemIsSelectable)
    
    self.setCursor(QCursor(Qt.SizeAllCursor))
    
    self.update_from_entity()
  
  def update_from_entity(self):
    if self.entity_class == "entity":
      self.init_entity()
    elif self.entity_class == "tile_entity":
      self.init_tile_entity()
    elif self.entity_class == "exit":
      self.init_exit()
    elif self.entity_class == "exit_region":
      self.init_exit_region()
  
  def init_entity(self):
    self.setPos(self.entity.x_pos, self.entity.y_pos)
    
    if self.entity.type == 3:
      self.setBrush(self.ENEMY_BRUSH)
    else:
      self.setBrush(self.ENTITY_BRUSH)
  
  def init_tile_entity(self):
    self.setPos(self.entity.x_pos*16+8, self.entity.y_pos*16+8)
    
    self.setBrush(self.TILE_ENTITY_BRUSH)
  
  def init_exit(self):
    ext = self.entity
    room = self.entity.room
    
    self.setPos(ext.x_pos, ext.y_pos)
    
    self.setBrush(self.EXIT_BRUSH)
    
    if ext.transition_type == 0:
      if ext.unknown_1 & 0x03 != 0:
        # Upwards screen edge transition
        self.setPos(0, 0 - ((ext.unknown_1 & 0x03) >> 0)*0x10)
        self.setRect(0, 0, room.width, 16)
      elif ext.unknown_1 & 0x0C != 0:
        # Rightwards screen edge transition
        self.setPos(room.width - 0x10 + ((ext.unknown_1 & 0x0C) >> 2)*0x10, 0)
        self.setRect(0, 0, 16, room.height)
      elif ext.unknown_1 & 0x30 != 0:
        # Downwards screen edge transition
        self.setPos(0, room.height - 0x10 + ((ext.unknown_1 & 0x30) >> 4)*0x10)
        self.setRect(0, 0, room.width, 16)
      elif ext.unknown_1 & 0xC0 != 0:
        # Leftwards screen edge transition
        self.setPos(0 - ((ext.unknown_1 & 0xC0) >> 6)*0x10, 0)
        self.setRect(0, 0, 16, room.height)
  
  def init_exit_region(self):
    self.setBrush(self.EXIT_BRUSH)
    
    self.setPos(self.entity.center_x, self.entity.center_y)
    self.setRect(-self.entity.half_width, -self.entity.half_height, self.entity.half_width*2, self.entity.half_height*2)
