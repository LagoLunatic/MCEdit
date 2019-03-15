
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

from mcedit_ui.custom_graphics_items import *

class EntityLayerItem(QGraphicsRectItem):
  def __init__(self, entity_lists, renderer, room_bg_palettes):
    super().__init__()
    
    self.entity_lists = entity_lists
    self.renderer = renderer
    self.room_bg_palettes = room_bg_palettes
    
    self.entity_graphics_items_by_entity_list = []
    z_value = 9999
    for entity_list in self.entity_lists:
      graphics_items_for_list = []
      self.entity_graphics_items_by_entity_list.append((entity_list, graphics_items_for_list))
      
      for entity in entity_list.entities:
        entity_item = self.add_graphics_item_for_entity(entity)
        graphics_items_for_list.append(entity_item)
        
        entity_item.setZValue(z_value)
        z_value -= 1
  
  def add_graphics_item_for_entity(self, entity):
    try:
      image = None
      if entity.type in [3, 4, 6, 7]:
        image = self.renderer.render_entity_sprite_frame(entity, self.room_bg_palettes)
      
      if image is None:
        entity_item = EntityRectItem(entity, "entity")
        entity_item.setParentItem(self)
      else:
        entity_item = EntityImageItem(image, entity, "entity")
        entity_item.setParentItem(self)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error rendering entity sprite in room %02X-%02X:\n" % (entity.room.area.area_index, entity.room.room_index)
      error_message += str(e) + "\n\n" + stack_trace
      with open("./wip/entity render error %02X-%02X-%02X.txt" % (entity.type, entity.subtype, entity.form), "w") as f:
        f.write(error_message)
      #print(error_message)
      
      entity_item = EntityRectItem(entity, "entity")
      entity_item.setParentItem(self)
    
    return entity_item
