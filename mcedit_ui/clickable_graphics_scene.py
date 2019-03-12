
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class ClickableGraphicsScene(QGraphicsScene):
  BACKGROUND_BRUSH = QBrush(QColor(240, 240, 240, 255))
  
  clicked = Signal(int, int, object)
  moved = Signal(int, int, object)
  released = Signal(int, int, object)
  
  def __init__(self):
    super().__init__()
    
    self.setBackgroundBrush(self.BACKGROUND_BRUSH)
  
  def mousePressEvent(self, event):
    x = int(event.scenePos().x())
    y = int(event.scenePos().y())
    self.clicked.emit(x, y, event.buttons())
    
    super().mousePressEvent(event)
  
  def mouseMoveEvent(self, event):
    x = int(event.scenePos().x())
    y = int(event.scenePos().y())
    self.moved.emit(x, y, event.buttons())
    
    super().mouseMoveEvent(event)
  
  def mouseReleaseEvent(self, event):
    x = int(event.scenePos().x())
    y = int(event.scenePos().y())
    self.released.emit(x, y, event.button())
    
    super().mouseReleaseEvent(event)
  
  def itemAt(self, x, y):
    return super().itemAt(x, y, QTransform())
