
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mcedit_ui.ui_entity_search import Ui_EntitySearch

from mclib.docs import Docs

import re

class EntitySearchDialog(QDialog):
  def __init__(self, main_window):
    super().__init__(main_window, Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)
    self.ui = Ui_EntitySearch()
    self.ui.setupUi(self)
    
    self.ui.find_button.clicked.connect(self.execute_search)
    self.ui.entity_list.currentRowChanged.connect(self.selected_entity_changed)
    self.ui.entity_list.clicked.connect(self.selected_entity_changed)
    
    self.show()
  
  def execute_search(self):
    game = self.parent().game
    
    self.ui.entity_list.clear()
    
    type = self.ui.type.text()
    if re.search(r"^[0-9a-f]+$", type, re.IGNORECASE):
      type = int(type, 16)
    else:
      type = None
    
    subtype = self.ui.subtype.text()
    if re.search(r"^[0-9a-f]+$", subtype, re.IGNORECASE):
      subtype = int(subtype, 16)
    else:
      subtype = None
    
    form = self.ui.form.text()
    if re.search(r"^[0-9a-f]+$", form, re.IGNORECASE):
      form = int(form, 16)
    else:
      form = None
    
    self.entities = []
    for area in game.areas:
      for room in area.rooms:
        if room is None:
          continue
        
        for entity_list in room.entity_lists:
          for entity in entity_list.entities:
            if type is not None and type != entity.type:
              continue
            if subtype is not None and subtype != entity.subtype:
              continue
            if form is not None and form != entity.form:
              continue
            
            self.entities.append(entity)
            self.ui.entity_list.addItem(
              "In room %02X-%02X:  Entity %02X-%02X-%02X  %s" % (
                room.area.area_index, room.room_index,
                entity.type, entity.subtype, entity.form,
                Docs.get_name_for_entity("entity", entity.type, entity.subtype, entity.form)
              ))
  
  def selected_entity_changed(self):
    index = self.ui.entity_list.currentRow()
    if index == -1:
      return
    entity = self.entities[index]
    
    self.parent().go_to_room_and_select_entity(entity)
