
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mcedit_ui.custom_graphics_items import *

class EntityLayerItem(QGraphicsRectItem):
  def __init__(self, entity_lists, renderer):
    super().__init__()
    
    self.entity_lists = entity_lists
    self.renderer = renderer
    
    self.entity_graphics_items_by_entity_list = []
    for entity_list in self.entity_lists:
      graphics_items_for_list = []
      self.entity_graphics_items_by_entity_list.append((entity_list, graphics_items_for_list))
      
      for entity in entity_list.entities:
        entity_item = self.add_graphics_item_for_entity(entity)
        graphics_items_for_list.append(entity_item)
  
  def add_graphics_item_for_entity(self, entity):
    if entity.type in [3, 4, 6, 7]:
      entity_item = EntityImageItem(entity, "entity", self.renderer)
    else:
      entity_item = EntityRectItem(entity, "entity")
    
    entity_item.setParentItem(self)
    
    return entity_item
