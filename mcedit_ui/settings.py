
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from mcedit_ui.uic.ui_settings import Ui_Settings

class SettingsDialog(QDialog):
  def __init__(self, main_window):
    super().__init__(main_window, Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)
    self.ui = Ui_Settings()
    self.ui.setupUi(self)
    
    self.settings = main_window.settings
    
    for save_slot in range(3):
      self.ui.test_room_save_slot.addItem("Slot %d" % (save_slot+1))
    
    self.ui.emulator_path.setText(self.settings.get("emulator_path"))
    self.ui.test_room_save_slot.setCurrentIndex(self.settings.get("test_room_save_slot_index", 0))
    
    self.ui.emulator_path_browse_button.clicked.connect(self.browse_for_emulator_path)
    self.ui.buttonBox.clicked.connect(self.button_pressed)
    
    self.show()
  
  def browse_for_emulator_path(self):
    default_dir = None
    emu_path, selected_filter = QFileDialog.getOpenFileName()
    if not emu_path:
      return
    
    self.ui.emulator_path.setText(emu_path)
  
  def button_pressed(self, button):
    if self.ui.buttonBox.standardButton(button) == QDialogButtonBox.Ok:
      self.settings["emulator_path"] = self.ui.emulator_path.text()
      self.settings["test_room_save_slot_index"] = self.ui.test_room_save_slot.currentIndex()
    
    self.close()
