
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mclib.docs import Docs

from collections import namedtuple
import string

Property = namedtuple(
  "Property",
  "pretty_name attribute_name num_bits"
)
ENTITY_PROPERTIES_BY_CLASS = {
  "entity": [
    Property("ROM Location", "entity_ptr", 32),
    Property("Type", "type", 4),
    Property("Unknown 1", "unknown_1", 4),
    Property("Unknown 2", "unknown_2", 4),
    Property("Unknown 3", "unknown_3", 4),
    Property("Subtype", "subtype", 8),
    Property("Form", "form", 8),
    Property("Unknown 4", "unknown_4", 8),
    Property("Unknown 5", "unknown_5", 8),
    Property("Unknown 6", "unknown_6", 8),
    Property("Unknown 7", "unknown_7", 8),
    Property("X Pos", "x_pos", 16),
    Property("Y Pos", "y_pos", 16),
    Property("Params", "params", 32),
  ],
  
  "tile_entity": [
    Property("ROM Location", "entity_ptr", 32),
    Property("Type", "type", 8),
    Property("Unknown 1", "unknown_1", 8),
    Property("Item ID", "item_id", 8),
    Property("Unknown 2", "unknown_2", 8),
    Property("X Pos", "x_pos", 6),
    Property("Y Pos", "y_pos", 6),
    Property("Unknown 3", "unknown_3", 4),
    Property("Message ID", "message_id", 16),
  ],
  
  "exit": [
    Property("ROM Location", "exit_ptr", 32),
    Property("Transition Type", "transition_type", 16),
    Property("X Pos", "x_pos", 16),
    Property("Y Pos", "y_pos", 16),
    Property("Dest X", "dest_x", 16),
    Property("Dest Y", "dest_y", 16),
    Property("Unknown 1", "unknown_1", 8),
    Property("Dest Area", "dest_area", 8),
    Property("Dest Room", "dest_room", 8),
    Property("Unknown 2", "unknown_2", 8),
    Property("Unknown 3", "unknown_3", 8),
    Property("Unknown 4", "unknown_4", 16),
    Property("Padding", "padding", 16),
  ],
  
  "exit_region": [
    Property("ROM Location", "region_ptr", 32),
    Property("Center X", "center_x", 16),
    Property("Center Y", "center_y", 16),
    Property("Width/2", "half_width", 8),
    Property("Height/2", "half_height", 8),
    Property("Which Exit", "exit_pointer_property_index", 8),
    Property("Unknown", "unknown_bitfield", 8),
    # TODO: how to display both the exit region AND the exit's properties at once?
  ],
}

class EntityProperties(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    
    v_layout = QVBoxLayout(self)
    
    self.entity_label = QLabel(self)
    self.entity_label.setText("(No entity selected.)")
    v_layout.addWidget(self.entity_label)
    
    self.properties_tree = QTreeView(self)
    delegate = CustomItemDelegate()
    self.properties_tree.setItemDelegate(delegate)
    self.entity_model = EntityModel()
    self.properties_tree.setModel(self.entity_model)
    self.properties_tree.hide()
    v_layout.addWidget(self.properties_tree)
  
  def select_entity_graphics_item(self, entity_graphics_item):
    if entity_graphics_item is None:
      self.entity_label.setText("(No entity selected.)")
      self.entity_model.entity = None
      self.properties_tree.hide()
      return
    
    self.properties_tree.show()
    
    self.entity_model.set_entity(entity_graphics_item)
    
    self.entity_model.layoutChanged.emit()
    
    entity_class = entity_graphics_item.entity_class
    if entity_class == "entity":
      self.entity_label.setText("Entity properties:")
    elif entity_class == "tile_entity":
      self.entity_label.setText("Tile entity properties:")
    elif entity_class == "exit":
      self.entity_label.setText("Exit properties:")
    elif entity_class == "exit_region":
      self.entity_label.setText("Exit region properties:")
    else:
      raise Exception("Unknown entity class: %s" % entity_class)

class CustomItemDelegate(QItemDelegate):
  def createEditor(self, parent, option, index):
    model = index.model()
    entity = model.entity
    prop = model.get_property_by_row(index.row())
    
    if prop.attribute_name in ["type", "subtype", "form"]:
      editor = QComboBox(parent)
      
      num_possible_values = 2**prop.num_bits
      for i in range(num_possible_values):
        option_name = Docs.prettify_prop_value(prop, i, entity)
        editor.addItem(option_name)
    else:
      editor = QLineEdit(parent)
    return editor
  
  def setEditorData(self, editor, index):
    prop = index.model().get_property_by_row(index.row())
    if prop.attribute_name in ["type", "subtype", "form"]:
      value_index = editor.findText(index.data())
      editor.setCurrentIndex(value_index)
    else:
      editor.setText(index.data())
  
  def setModelData(self, editor, model, index):
    prop = index.model().get_property_by_row(index.row())
    if prop.attribute_name in ["type", "subtype", "form"]:
      value = editor.currentIndex()
    else:
      value = editor.text()
      if not all(char in string.hexdigits for char in value):
        return
      value = int(value, 16)
    
    max_val = (2 << prop.num_bits) - 1
    if value > max_val:
      value = max_val
    if value < 0:
      value = 0
    
    model.entity.__dict__[prop.attribute_name] = value
    model.entity_graphics_item.update_from_entity()

class EntityModel(QAbstractItemModel):
  def __init__(self, parent=None):
    super().__init__(parent)
    
    self.entity = None
    self.entity_class = None
  
  def set_entity(self, entity_graphics_item):
    self.entity_graphics_item = entity_graphics_item
    self.entity = entity_graphics_item.entity
    self.entity_class = entity_graphics_item.entity_class
    
    self.properties = ENTITY_PROPERTIES_BY_CLASS[self.entity_class]
  
  def columnCount(self, parent):
    # Property name, property value
    return 2
  
  def rowCount(self, parent):
    if parent.isValid():
      # The properties don't have any children of their own.
      return 0
    else:
      # The root node. Return the number of properties.
      if self.entity is None:
        return 0
      
      return len(self.properties)
  
  def headerData(self, section, orientation, role):
    if role == Qt.DisplayRole:
      if section == 0:
        return "Property"
      else:
        return "Value"
    else:
      return None
  
  def data(self, index, role):
    if not index.isValid():
      return None
    
    if role == Qt.DisplayRole:
      if self.entity is None:
        return None
      
      prop = self.get_property_by_row(index.row())
      
      if index.column() == 0:
        return prop.pretty_name
      else:
        value = self.entity.__dict__[prop.attribute_name]
        return Docs.prettify_prop_value(prop, value, self.entity)
    else:
      return None
  
  def get_property_by_row(self, row):
    if self.entity is None:
      return (None, None, None)
    
    return self.properties[row]
  
  def index(self, row, column, parent):
    if self.hasIndex(row, column, parent):
      return self.createIndex(row, column)
    else:
      return QModelIndex()
  
  def parent(self, index):
    return QModelIndex()
  
  def flags(self, index):
    prop = self.get_property_by_row(index.row())
    if index.column() == 0 or prop.pretty_name == "ROM Location":
      return Qt.ItemIsEnabled | Qt.ItemNeverHasChildren
    else:
      return Qt.ItemIsEnabled | Qt.ItemNeverHasChildren | Qt.ItemIsEditable
