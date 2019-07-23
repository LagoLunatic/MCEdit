# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui',
# licensing of 'settings.ui' applies.
#
# Created: Tue Jul 23 15:29:50 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(600, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Settings)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.emulator_path = QtWidgets.QLineEdit(Settings)
        self.emulator_path.setObjectName("emulator_path")
        self.gridLayout.addWidget(self.emulator_path, 0, 1, 1, 1)
        self.emulator_path_browse_button = QtWidgets.QPushButton(Settings)
        self.emulator_path_browse_button.setObjectName("emulator_path_browse_button")
        self.gridLayout.addWidget(self.emulator_path_browse_button, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Settings)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.test_room_save_slot = QtWidgets.QComboBox(Settings)
        self.test_room_save_slot.setMaximumSize(QtCore.QSize(80, 16777215))
        self.test_room_save_slot.setObjectName("test_room_save_slot")
        self.gridLayout.addWidget(self.test_room_save_slot, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Settings)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtWidgets.QApplication.translate("Settings", "Entity Search", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Settings", "Test Room Emulator Path", None, -1))
        self.emulator_path_browse_button.setText(QtWidgets.QApplication.translate("Settings", "Browse", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Settings", "Test Room Save Slot", None, -1))

