# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_editor.ui',
# licensing of 'text_editor.ui' applies.
#
# Created: Thu Apr 18 13:30:48 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TextEditor(object):
    def setupUi(self, TextEditor):
        TextEditor.setObjectName("TextEditor")
        TextEditor.resize(1024, 720)
        self.verticalLayout = QtWidgets.QVBoxLayout(TextEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.message_group_index = QtWidgets.QComboBox(TextEditor)
        self.message_group_index.setObjectName("message_group_index")
        self.horizontalLayout_2.addWidget(self.message_group_index)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message_list = QtWidgets.QListWidget(TextEditor)
        self.message_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.message_list.setObjectName("message_list")
        self.horizontalLayout.addWidget(self.message_list)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(TextEditor)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.rom_location = QtWidgets.QLineEdit(TextEditor)
        self.rom_location.setMaximumSize(QtCore.QSize(80, 16777215))
        self.rom_location.setReadOnly(True)
        self.rom_location.setObjectName("rom_location")
        self.horizontalLayout_3.addWidget(self.rom_location)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.message_text_edit = QtWidgets.QTextEdit(TextEditor)
        self.message_text_edit.setObjectName("message_text_edit")
        self.verticalLayout_2.addWidget(self.message_text_edit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(TextEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TextEditor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TextEditor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TextEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(TextEditor)

    def retranslateUi(self, TextEditor):
        TextEditor.setWindowTitle(QtWidgets.QApplication.translate("TextEditor", "Text Editor", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("TextEditor", "ROM Location", None, -1))

