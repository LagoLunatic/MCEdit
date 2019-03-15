
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

from mcedit_ui.custom_graphics_items import *

from mclib.entity_type_docs import EntityTypeDocs

class EntityLayerItem(QGraphicsRectItem):
  def __init__(self, entity_list, renderer, room_bg_palettes):
    super().__init__()
    
    self.entity_list = entity_list
    self.renderer = renderer
    self.room_bg_palettes = room_bg_palettes
    
    for entity in self.entity_list.entities:
      self.add_graphics_item_for_entity(entity)
  
  def add_graphics_item_for_entity(self, entity):
    try:
      if entity.type in [3, 4, 6, 7]:
        best_frame_index = EntityTypeDocs.get_best_sprite_frame(entity)
        image = self.renderer.render_entity_sprite_frame(entity, self.room_bg_palettes, best_frame_index)
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
