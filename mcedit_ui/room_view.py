
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class RoomView(QGraphicsView):
  ZOOM_SCALES = [
    0.25,
    0.5,
    0.75,
    1.0,
    1.5,
    2.0,
    2.5,
    3.0,
    4.0,
  ]
  
  def __init__(self, parent):
    super().__init__(parent)
    
    self.is_panning = False
    self.curr_zoom_index = self.ZOOM_SCALES.index(1.0)
    
    self.setMouseTracking(True)
  
  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Space and not event.isAutoRepeat():
      self.set_panning(True)
  
  def keyReleaseEvent(self, event):
    if event.key() == Qt.Key_Space and not event.isAutoRepeat():
      self.set_panning(False)
  
  def set_panning(self, is_panning):
    if is_panning == self.is_panning:
      return
    
    self.is_panning = is_panning
    
    self.setInteractive(not is_panning)
    
    if is_panning:
      self.orig_mouse_pos = QCursor.pos()
      QApplication.setOverrideCursor(QCursor(Qt.ClosedHandCursor))
      #viewport.grabMouse()
    else:
      #viewport.releaseMouse()
      QApplication.restoreOverrideCursor()
  
  def mouseMoveEvent(self, event):
    if self.is_panning:
      diff = event.globalPos() - self.orig_mouse_pos

      horizontalValue = self.horizontalScrollBar().value() - diff.x()
      verticalValue = self.verticalScrollBar().value() - diff.y()

      self.horizontalScrollBar().setValue(horizontalValue)
      self.verticalScrollBar().setValue(verticalValue)

      self.orig_mouse_pos = event.globalPos()
    else:
      super().mouseMoveEvent(event)
      self.orig_mouse_pos = event.globalPos()
  
  def mousePressEvent(self, event):
    if event.button() == Qt.MiddleButton:
      self.set_panning(True)
      return
    
    super().mousePressEvent(event)
  
  def mouseReleaseEvent(self, event):
    if event.button() == Qt.MiddleButton:
      self.set_panning(False)
      return
    
    super().mouseReleaseEvent(event)
  
  def wheelEvent(self, event):
    if not QApplication.keyboardModifiers() & Qt.ControlModifier:
      return
    
    y_change = event.angleDelta().y()
    
    if y_change > 0:
      if self.curr_zoom_index == len(self.ZOOM_SCALES) - 1:
        return
      self.curr_zoom_index += 1
    elif y_change < 0:
      if self.curr_zoom_index == 0:
        return
      self.curr_zoom_index -= 1
    else:
      return
    
    curr_zoom_scale = self.ZOOM_SCALES[self.curr_zoom_index]
    self.resetTransform()
    self.scale(curr_zoom_scale, curr_zoom_scale)
