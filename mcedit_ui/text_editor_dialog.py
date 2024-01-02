
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from mcedit_ui.uic.ui_text_editor import Ui_TextEditor

from mclib.message import Message, MessageGroup

import re

class TextEditorDialog(QDialog):
  def __init__(self, main_window):
    super().__init__(main_window)
    self.ui = Ui_TextEditor()
    self.ui.setupUi(self)
    
    self.rom = main_window.game.rom
    
    self.ui.message_group_index.activated.connect(self.message_group_changed)
    self.ui.message_list.currentRowChanged.connect(self.message_changed)
    
    self.message_groups = []
    self.group_index = None
    self.message_index = None
    
    for group_index in range(0x50):
      self.ui.message_group_index.addItem("%02X" % group_index)
      
      message_group = MessageGroup(group_index, self.rom)
      self.message_groups.append(message_group)
      
      for message_index in range(message_group.num_messages):
        message_id = (group_index << 8) | message_index
        message = Message(message_id, self.rom)
    
    self.show()
    
    self.message_group_changed(0)
  
  def message_group_changed(self, group_index):
    self.ui.message_list.clear()
    
    self.group_index = group_index
    self.group_messages = []
    self.group = self.message_groups[self.group_index]
    
    font_metrics = QFontMetrics(self.ui.message_list.font())
    max_preview_str_width = self.ui.message_list.viewport().width() - self.ui.message_list.verticalScrollBar().width()
    
    for message_index in range(self.group.num_messages):
      message_id = (group_index << 8) | message_index
      message = Message(message_id, self.rom)
      self.group_messages.append(message)
      
      preview_string = "%02X " % message_index
      preview_string += message.string.replace("\\n\n", " ")
      preview_string = font_metrics.elidedText(preview_string, Qt.TextElideMode.ElideRight, max_preview_str_width)
      self.ui.message_list.addItem(preview_string)
  
  def message_changed(self, message_index):
    self.message_index = message_index
    
    message = self.group_messages[message_index]
    
    self.ui.message_text_edit.setText(message.string)
    self.ui.rom_location.setText("%08X" % message.string_ptr)
