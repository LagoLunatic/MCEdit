
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import traceback

from mcedit_ui.ui_save_editor import Ui_SaveEditor

from mclib.data_interface import DataInterface
from mclib.save import Save, SaveSlot
from mclib.docs import ITEM_ID_TO_NAME

class SaveEditorDialog(QDialog):
  def __init__(self, main_window):
    super().__init__(main_window)
    self.ui = Ui_SaveEditor()
    self.ui.setupUi(self)
    
    self.rom = main_window.game.rom
    
    self.save = None
    
    self.ui.import_raw_save.clicked.connect(self.import_raw_save)
    self.ui.import_vba_mgba_save.clicked.connect(self.import_vba_mgba_save)
    self.ui.import_gameshark_save.clicked.connect(self.import_gameshark_save)
    self.ui.export_raw_save.clicked.connect(self.export_raw_save)
    self.ui.export_vba_mgba_save.clicked.connect(self.export_vba_mgba_save)
    self.ui.export_gameshark_save.clicked.connect(self.export_gameshark_save)
    
    self.selected_slot_index = 0
    self.ui.selected_slot_index.activated.connect(self.selected_slot_index_changed)
    
    self.initialize_ui_lists()
    
    self.show()
  
  def selected_slot_index_changed(self, new_slot_index):
    self.update_save_from_ui() # Save changes to the previously slot UI to the save.
    self.selected_slot_index = new_slot_index
    self.update_ui_from_save() # Load the new slot's data from the save to the UI.
  
  def initialize_ui_lists(self):
    figs_layout = self.ui.owned_figurines_layout
    for fig_id in range(SaveSlot.NUM_FIGURINES):
      checkbox = QCheckBox(self)
      checkbox.setText("Figurine %d" % (fig_id))
      figs_layout.addWidget(checkbox)
    spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    figs_layout.addItem(spacer)
    
    items_layout = self.ui.owned_items_layout
    for item_id in range(SaveSlot.NUM_ITEMS):
      item_name = ITEM_ID_TO_NAME.get(item_id, "")
      
      label = QLabel(self)
      label.setText("%02X %s" % (item_id, item_name))
      items_layout.setWidget(item_id, QFormLayout.LabelRole, label)
      
      dropdown = QComboBox(self)
      dropdown.addItem("Not owned")
      dropdown.addItem("Owned")
      dropdown.addItem("Formerly owned")
      dropdown.addItem("(Unused)")
      items_layout.setWidget(item_id, QFormLayout.FieldRole, dropdown)
    
    flags_layout = self.ui.flags_layout
    self.flag_checkboxes = []
    all_local_flag_offsets = [
      (0x0000, "Global"),
      (0x0100, "Outdoors"),
      (0x0200, "Indoors"),
      (0x0300, "Caves & Passages"),
      (0x0400, "Caves"),
      (0x0500, "Deepwood Shrine"),
      (0x05C0, "Cave of Flames"),
      (0x0680, "Fortress of Winds"),
      (0x0740, "Temple of Droplets"),
      (0x0800, "Palace of Winds"),
      (0x08C0, "Dark Hyrule Castle"),
      (0x09C0, "(Unused 1)"),
      (0x0A80, "(Unused 2)"),
      (0x1000, ""),
    ]
    col = 0
    for i in range(len(all_local_flag_offsets)-1):
      local_flag_offset, flag_region_name = all_local_flag_offsets[i]
      next_local_flag_offset, next_flag_region_name = all_local_flag_offsets[i+1]
      
      label = QLabel()
      label.setText(flag_region_name)
      flags_layout.addWidget(label, 0, col)
      
      row = 1
      for flag_index in range(local_flag_offset, next_local_flag_offset):
        checkbox = QCheckBox(self)
        checkbox.setText("Flag %03X" % (flag_index))
        flags_layout.addWidget(checkbox, row, col)
        self.flag_checkboxes.append(checkbox)
        row += 1
      col += 1
  
  def update_ui_from_save(self):
    if self.save is None:
      return
    
    slot = self.save.slots[self.selected_slot_index]
    
    figs_layout = self.ui.owned_figurines_layout
    for fig_id, fig_is_owned in enumerate(slot.owned_figurines):
      checkbox = figs_layout.itemAt(fig_id).widget()
      checkbox.setChecked(fig_is_owned)
    
    items_layout = self.ui.owned_items_layout
    for item_id, owned_item_value in enumerate(slot.owned_item_info):
      dropdown = items_layout.itemAt(item_id, QFormLayout.FieldRole).widget()
      dropdown.setCurrentIndex(owned_item_value)
    
    for flag_index, flag_is_set in enumerate(slot.flags):
      checkbox = self.flag_checkboxes[flag_index]
      checkbox.setChecked(flag_is_set)
  
  def update_save_from_ui(self):
    if self.save is None:
      return
    
    slot = self.save.slots[self.selected_slot_index]
    
    figs_layout = self.ui.owned_figurines_layout
    for fig_id, fig_is_owned in enumerate(slot.owned_figurines):
      checkbox = figs_layout.itemAt(fig_id).widget()
      slot.owned_figurines[fig_id] = checkbox.isChecked()
    
    items_layout = self.ui.owned_items_layout
    for item_id, owned_item_value in enumerate(slot.owned_item_info):
      dropdown = items_layout.itemAt(item_id, QFormLayout.FieldRole).widget()
      slot.owned_item_info[item_id] = dropdown.currentIndex()
    
    for flag_index, flag_is_set in enumerate(slot.flags):
      checkbox = self.flag_checkboxes[flag_index]
      slot.flags[flag_index] = checkbox.isChecked()
  
  
  def get_import_path(self):
    default_dir = None
    file_path, selected_filter = QFileDialog.getOpenFileName(self, "Select save to open", default_dir, "Save Files (*.sav)")
    return file_path
  
  def get_export_path(self):
    if self.save is None:
      QMessageBox.warning(self,
        "No save data loaded",
        "Must import a save before you can export it."
      )
      return None
    
    default_dir = None
    file_path, selected_filter = QFileDialog.getSaveFileName(self, "Select where to export save", default_dir, "Save Files (*.sav)")
    return file_path
  
  def import_raw_save(self):
    file_path = self.get_import_path()
    if not file_path:
      return
    
    try:
      with open(file_path, "rb") as f:
        data = DataInterface(f.read())
      self.save = Save.from_raw_format(data)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error importing save:\n" + str(e) + "\n\n" + stack_trace
      QMessageBox.critical(self,
        "Error importing save",
        error_message
      )
      return
    
    self.update_ui_from_save()
  
  def import_vba_mgba_save(self):
    file_path = self.get_import_path()
    if not file_path:
      return
    
    try:
      with open(file_path, "rb") as f:
        data = DataInterface(f.read())
      self.save = Save.from_vba_mgba_format(data)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error importing save:\n" + str(e) + "\n\n" + stack_trace
      QMessageBox.critical(self,
        "Error importing save",
        error_message
      )
      return
    
    self.update_ui_from_save()
  
  def import_gameshark_save(self):
    file_path = self.get_import_path()
    if not file_path:
      return
    
    try:
      with open(file_path, "rb") as f:
        data = DataInterface(f.read())
      self.save = Save.from_gameshark_format(data)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error importing save:\n" + str(e) + "\n\n" + stack_trace
      QMessageBox.critical(self,
        "Error importing save",
        error_message
      )
      return
    
    self.update_ui_from_save()
  
  def export_raw_save(self):
    file_path = self.get_export_path()
    if not file_path:
      return
    
    try:
      self.update_save_from_ui()
      self.save.write()
      raw_bytes = self.save.to_raw_format().read_all_bytes()
      with open(file_path, "wb") as f:
        f.write(raw_bytes)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error exporting save:\n" + str(e) + "\n\n" + stack_trace
      QMessageBox.critical(self,
        "Error exporting save",
        error_message
      )
      return
  
  def export_vba_mgba_save(self):
    file_path = self.get_export_path()
    if not file_path:
      return
    
    try:
      self.update_save_from_ui()
      self.save.write()
      raw_bytes = self.save.to_vba_mgba_format().read_all_bytes()
      with open(file_path, "wb") as f:
        f.write(raw_bytes)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error exporting save:\n" + str(e) + "\n\n" + stack_trace
      QMessageBox.critical(self,
        "Error exporting save",
        error_message
      )
      return
  
  def export_gameshark_save(self):
    file_path = self.get_export_path()
    if not file_path:
      return
    
    try:
      self.update_save_from_ui()
      self.save.write()
      raw_bytes = self.save.to_gameshark_format().read_all_bytes()
      with open(file_path, "wb") as f:
        f.write(raw_bytes)
    except Exception as e:
      stack_trace = traceback.format_exc()
      error_message = "Error exporting save:\n" + str(e) + "\n\n" + stack_trace
      QMessageBox.critical(self,
        "Error exporting save",
        error_message
      )
      return
