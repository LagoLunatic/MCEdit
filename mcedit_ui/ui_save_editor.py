# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_editor.ui',
# licensing of 'save_editor.ui' applies.
#
# Created: Mon Apr 15 12:55:13 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SaveEditor(object):
    def setupUi(self, SaveEditor):
        SaveEditor.setObjectName("SaveEditor")
        SaveEditor.resize(1024, 720)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_raw_save = QtWidgets.QPushButton(SaveEditor)
        self.import_raw_save.setObjectName("import_raw_save")
        self.horizontalLayout.addWidget(self.import_raw_save)
        self.import_vba_mgba_save = QtWidgets.QPushButton(SaveEditor)
        self.import_vba_mgba_save.setObjectName("import_vba_mgba_save")
        self.horizontalLayout.addWidget(self.import_vba_mgba_save)
        self.import_gameshark_save = QtWidgets.QPushButton(SaveEditor)
        self.import_gameshark_save.setObjectName("import_gameshark_save")
        self.horizontalLayout.addWidget(self.import_gameshark_save)
        self.export_raw_save = QtWidgets.QPushButton(SaveEditor)
        self.export_raw_save.setObjectName("export_raw_save")
        self.horizontalLayout.addWidget(self.export_raw_save)
        self.export_vba_mgba_save = QtWidgets.QPushButton(SaveEditor)
        self.export_vba_mgba_save.setObjectName("export_vba_mgba_save")
        self.horizontalLayout.addWidget(self.export_vba_mgba_save)
        self.export_gameshark_save = QtWidgets.QPushButton(SaveEditor)
        self.export_gameshark_save.setObjectName("export_gameshark_save")
        self.horizontalLayout.addWidget(self.export_gameshark_save)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selected_slot_index = QtWidgets.QComboBox(SaveEditor)
        self.selected_slot_index.setMinimumSize(QtCore.QSize(100, 0))
        self.selected_slot_index.setObjectName("selected_slot_index")
        self.selected_slot_index.addItem("")
        self.selected_slot_index.addItem("")
        self.selected_slot_index.addItem("")
        self.horizontalLayout_2.addWidget(self.selected_slot_index)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(SaveEditor)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1000, 628))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.owned_figurines_layout = QtWidgets.QVBoxLayout()
        self.owned_figurines_layout.setObjectName("owned_figurines_layout")
        self.horizontalLayout_3.addLayout(self.owned_figurines_layout)
        self.owned_items_layout = QtWidgets.QFormLayout()
        self.owned_items_layout.setObjectName("owned_items_layout")
        self.horizontalLayout_3.addLayout(self.owned_items_layout)
        self.flags_layout = QtWidgets.QVBoxLayout()
        self.flags_layout.setObjectName("flags_layout")
        self.horizontalLayout_3.addLayout(self.flags_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(SaveEditor)
        QtCore.QMetaObject.connectSlotsByName(SaveEditor)

    def retranslateUi(self, SaveEditor):
        SaveEditor.setWindowTitle(QtWidgets.QApplication.translate("SaveEditor", "Save Editor", None, -1))
        self.import_raw_save.setText(QtWidgets.QApplication.translate("SaveEditor", "Import Raw Save", None, -1))
        self.import_vba_mgba_save.setText(QtWidgets.QApplication.translate("SaveEditor", "Import VBA/mGBA Save", None, -1))
        self.import_gameshark_save.setText(QtWidgets.QApplication.translate("SaveEditor", "Import GameShark Save", None, -1))
        self.export_raw_save.setText(QtWidgets.QApplication.translate("SaveEditor", "Export Raw Save", None, -1))
        self.export_vba_mgba_save.setText(QtWidgets.QApplication.translate("SaveEditor", "Export VBA/mGBA Save", None, -1))
        self.export_gameshark_save.setText(QtWidgets.QApplication.translate("SaveEditor", "Export GameShark Save", None, -1))
        self.selected_slot_index.setItemText(0, QtWidgets.QApplication.translate("SaveEditor", "Save Slot 1", None, -1))
        self.selected_slot_index.setItemText(1, QtWidgets.QApplication.translate("SaveEditor", "Save Slot 2", None, -1))
        self.selected_slot_index.setItemText(2, QtWidgets.QApplication.translate("SaveEditor", "Save Slot 3", None, -1))

