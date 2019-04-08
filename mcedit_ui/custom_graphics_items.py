
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

class GenericEntityGraphicsItem(QGraphicsItem):
  def __init__(self, entity, entity_class):
    self.entity = entity
    self.entity_class = entity_class
    
    self.setFlag(QGraphicsItem.ItemIsMovable)
    self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
    self.setFlag(QGraphicsItem.ItemIsSelectable)
    
    self.setCursor(QCursor(Qt.SizeAllCursor))
    
    self.update_from_entity()
    
    self.setZValue(self.pos().y())
  
  def itemChange(self, change, value):
    if change == QGraphicsItem.ItemPositionChange and self.scene():
      new_pos = value
      x = new_pos.x()
      y = new_pos.y()
      
      if not QApplication.keyboardModifiers() & Qt.ControlModifier:
        # Lock to 8x8 grid unless Ctrl is held down
        x = round(x // 8) * 8
        y = round(y // 8) * 8
      
      x = int(x)
      y = int(y)
      
      # TODO: handle negatives better
      self.entity.x = x
      self.entity.y = y
      self.entity.save()
      
      new_pos.setX(self.entity.x)
      new_pos.setY(self.entity.y)
      
      self.setZValue(self.entity.y)
      
      self.scene().graphics_item_moved.emit(self)
      
      return super().itemChange(change, new_pos)
    
    return super().itemChange(change, value)

class GraphicsImageItem(QGraphicsPixmapItem):
  def __init__(self, pil_image=None):
    super().__init__()
    
    self.set_image(pil_image)
  
  def set_image(self, pil_image, x_off=0, y_off=0):
    if pil_image is None:
      width = 16
      height = 16
      pixmap = QPixmap(width, height)
      pixmap.fill(QColor(200, 0, 200, 150))
      self.setPixmap(pixmap)
      
      self.setOffset(-width//2, -height//2)
    else:
      width, height = pil_image.size
      data = pil_image.tobytes('raw', 'BGRA')
      qimage = QImage(data, width, height, QImage.Format_ARGB32)
      pixmap = QPixmap.fromImage(qimage)
      self.setPixmap(pixmap)
      
      self.setOffset(x_off, y_off)
  
  def boundingRect(self):
    # If the sprite is smaller than 16x16, make sure the bounding rectangle is at least 16x16.
    
    orig_rect = super().boundingRect()
    top = orig_rect.top()
    bottom = orig_rect.bottom()
    left = orig_rect.left()
    right = orig_rect.right()
    
    width = bottom - top
    height = right - left
    if width < 8:
      left -= (8-width)//2
      right += (8-width)//2
    if height < 8:
      top -= (8-height)//2
      bottom += (8-height)//2
    
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

class EntityImageItem(GraphicsImageItem, GenericEntityGraphicsItem):
  def __init__(self, entity, entity_class, renderer):
    self.renderer = renderer
    
    GraphicsImageItem.__init__(self)
    GenericEntityGraphicsItem.__init__(self, entity, entity_class)
  
  def update_from_entity(self):
    try:
      image, x_off, y_off = self.renderer.render_entity_pretty_sprite(self.entity)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error rendering entity sprite in room %02X-%02X:\n" % (
        self.entity.room.area.area_index, self.entity.room.room_index
      )
      error_message += str(e) + "\n\n" + stack_trace
      error_log_file_name = "./logs/entity render errors/entity render error %02X-%02X-%02X.txt" % (
        self.entity.type, self.entity.subtype, self.entity.form
      )
      with open(error_log_file_name, "w") as f:
        f.write(error_message)
      #print(error_message)
      
      image, x_off, y_off = (None, None, None)
    
    self.set_image(image, x_off, y_off)
    
    self.setPos(self.entity.x, self.entity.y)

class EntityRectItem(QGraphicsRectItem, GenericEntityGraphicsItem):
  ENTITY_BRUSH = QBrush(QColor(200, 0, 200, 150))
  TILE_ENTITY_BRUSH = QBrush(QColor(0, 0, 200, 150))
  EXIT_BRUSH = QBrush(QColor(200, 200, 200, 150))
  ENEMY_BRUSH = QBrush(QColor(200, 0, 0, 150))
  
  def __init__(self, entity, entity_class):
    QGraphicsRectItem.__init__(self, -8, -8, 16, 16)
    GenericEntityGraphicsItem.__init__(self, entity, entity_class)
  
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
    self.setPos(self.entity.x, self.entity.y)
    
    if self.entity.type == 3:
      self.setBrush(self.ENEMY_BRUSH)
    else:
      self.setBrush(self.ENTITY_BRUSH)
  
  def init_tile_entity(self):
    self.setPos(self.entity.x, self.entity.y)
    
    self.setRect(0, 0, 16, 16)
    
    self.setBrush(self.TILE_ENTITY_BRUSH)
  
  def init_exit(self):
    ext = self.entity
    room = self.entity.room
    
    self.setPos(ext.x, ext.y)
    
    self.setBrush(self.EXIT_BRUSH)
    
    self.setFlag(QGraphicsItem.ItemIsMovable)
    if ext.transition_type == 0:
      # Screen edge based exit transition.
      
      # Should not be draggable.
      self.setFlag(QGraphicsItem.ItemIsMovable, enabled=False)
      
      dir = None
      bits = None
      for i in range(4):
        bit_shift = i*2
        bit_mask = (3 << bit_shift)
        if (ext.screen_edge & bit_mask) != 0:
          dir = i
          bits = (ext.screen_edge & bit_mask) >> bit_shift
          break
      # TODO: what to do when more than one direction is set?
      
      if dir in [0, 2]:
        if dir == 0:
          # Up
          y = -16
        elif dir == 2:
          # Down
          y = room.height
        
        x = 0
        w = room.width
        
        if bits == 1:
          w //= 2
        elif bits == 2:
          w //= 2
          x += w
        
        self.setPos(x, y)
        self.setRect(0, 0, w, 16)
      elif dir in [1, 3]:
        if dir == 1:
          # Right
          x = room.width
        elif dir == 3:
          # Left
          x = -16
        
        y = 0
        h = room.height
        
        if bits == 1:
          h //= 2
        elif bits == 2:
          h //= 2
          y += h
        
        self.setPos(x, y)
        self.setRect(0, 0, 16, h)
      else:
        # No direction bits are set.
        # TODO: How to represent this invalid state visually?
        pass
  
  def init_exit_region(self):
    self.setBrush(self.EXIT_BRUSH)
    
    self.setPos(self.entity.center_x, self.entity.center_y)
    self.setRect(-self.entity.half_width, -self.entity.half_height, self.entity.half_width*2, self.entity.half_height*2)
