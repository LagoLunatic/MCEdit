# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entity_search.ui',
# licensing of 'entity_search.ui' applies.
#
# Created: Sat Mar 16 20:31:57 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_EntitySearch(object):
    def setupUi(self, EntitySearch):
        EntitySearch.setObjectName("EntitySearch")
        EntitySearch.resize(600, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(EntitySearch)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(EntitySearch)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(EntitySearch)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(EntitySearch)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.type = QtWidgets.QLineEdit(EntitySearch)
        self.type.setObjectName("type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.type)
        self.subtype = QtWidgets.QLineEdit(EntitySearch)
        self.subtype.setObjectName("subtype")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subtype)
        self.form = QtWidgets.QLineEdit(EntitySearch)
        self.form.setObjectName("form")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.form)
        self.verticalLayout.addLayout(self.formLayout)
        self.find_button = QtWidgets.QPushButton(EntitySearch)
        self.find_button.setObjectName("find_button")
        self.verticalLayout.addWidget(self.find_button)
        self.entity_list = QtWidgets.QListWidget(EntitySearch)
        self.entity_list.setObjectName("entity_list")
        self.verticalLayout.addWidget(self.entity_list)

        self.retranslateUi(EntitySearch)
        QtCore.QMetaObject.connectSlotsByName(EntitySearch)

    def retranslateUi(self, EntitySearch):
        EntitySearch.setWindowTitle(QtWidgets.QApplication.translate("EntitySearch", "Entity Search", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("EntitySearch", "Type", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("EntitySearch", "Subtype", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("EntitySearch", "Form", None, -1))
        self.find_button.setText(QtWidgets.QApplication.translate("EntitySearch", "Find", None, -1))

