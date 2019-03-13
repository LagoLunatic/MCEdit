
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

from mcedit_ui.custom_graphics_items import *

class EntityLayerItem(QGraphicsRectItem):
  def __init__(self, entity_list, renderer):
    super().__init__()
    
    self.entity_list = entity_list
    self.renderer = renderer
    
    for entity in self.entity_list.entities:
      self.add_graphics_item_for_entity(entity)
  
  def add_graphics_item_for_entity(self, entity):
    try:
      if entity.type in [3, 4, 6, 7]:
        image = self.renderer.render_entity_sprite(entity)
        entity_item = EntityImageItem(image, entity, "entity")
        entity_item.setParentItem(self)
      else:
        entity_item = EntityRectItem(entity, "entity")
        entity_item.setParentItem(self)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error rendering entity sprite:\n" + str(e) + "\n\n" + stack_trace
      print(error_message)
      
      entity_item = EntityRectItem(entity, "entity")
      entity_item.setParentItem(self)
