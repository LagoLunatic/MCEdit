
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from mclib.docs import Docs
from mclib.entity import ParamEntity

from collections import OrderedDict
import string

# TODO: tree widget isn't that great here after all... gotta make a fully custom thing so that comboboxes can be scrolled through easier

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
      self.entity_model.set_entity(None)
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
    
    if prop.attribute_name in ["type", "subtype", "form", "item_id"]:
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
    if prop.attribute_name in ["type", "subtype", "form", "item_id"]:
      value_index = editor.findText(index.data())
      editor.setCurrentIndex(value_index)
    else:
      editor.setText(index.data())
  
  def setModelData(self, editor, model, index):
    prop = index.model().get_property_by_row(index.row())
    if prop.attribute_name in ["type", "subtype", "form", "item_id"]:
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
    
    setattr(model.entity, prop.attribute_name, value)
    model.entity.update_params()
    model.entity_graphics_item.update_from_entity()

class EntityModel(QAbstractItemModel):
  def __init__(self, parent=None):
    super().__init__(parent)
    
    self.scene_graphics_item_moved_signal_connected = False
    
    self.set_entity(None)
  
  def set_entity(self, entity_graphics_item):
    if entity_graphics_item is None:
      self.entity_graphics_item = None
      self.entity = None
      self.entity_class = None
      self.properties = OrderedDict()
      return
    
    if not self.scene_graphics_item_moved_signal_connected:
      # Connect the scene's signal for updating the entity's position when it's moved.
      # This can't be connected in __init__ because we don't know what the scene is yet.
      # So instead we do it the first time an entity is selected.
      entity_graphics_item.scene().graphics_item_moved.connect(self.entity_moved)
    
    self.entity_graphics_item = entity_graphics_item
    self.entity = entity_graphics_item.entity
    self.entity_class = entity_graphics_item.entity_class
    
    self.properties = self.entity.properties
  
  def entity_moved(self, moved_graphics_item):
    if moved_graphics_item == self.entity_graphics_item:
      x_and_y_pos_row_indexes = [
        i for i, prop in enumerate(self.properties.values())
        if prop.pretty_name in ["X Pos", "Y Pos", "Tile X", "Tile Y"]
      ]
      
      if x_and_y_pos_row_indexes:
        first_row_index = min(x_and_y_pos_row_indexes)
        last_row_index = max(x_and_y_pos_row_indexes)
        top_left_model_index = self.index(first_row_index, 1)
        bottom_right_model_index = self.index(last_row_index, 1)
        
        self.dataChanged.emit(top_left_model_index, bottom_right_model_index)
  
  def columnCount(self, parent=QModelIndex()):
    # Property name, property value
    return 2
  
  def rowCount(self, parent=QModelIndex()):
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
        value = getattr(self.entity, prop.attribute_name)
        return Docs.prettify_prop_value(prop, value, self.entity)
    else:
      return None
  
  def get_property_by_row(self, row):
    if self.entity is None:
      return (None, None, None)
    
    return list(self.properties.values())[row]
  
  def index(self, row, column, parent=QModelIndex()):
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
