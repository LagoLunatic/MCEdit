# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'entity_search.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_EntitySearch(object):
    def setupUi(self, EntitySearch):
        if not EntitySearch.objectName():
            EntitySearch.setObjectName(u"EntitySearch")
        EntitySearch.resize(600, 500)
        self.verticalLayout = QVBoxLayout(EntitySearch)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EntitySearch)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(EntitySearch)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(EntitySearch)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.type = QLineEdit(EntitySearch)
        self.type.setObjectName(u"type")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.type)

        self.subtype = QLineEdit(EntitySearch)
        self.subtype.setObjectName(u"subtype")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.subtype)

        self.form = QLineEdit(EntitySearch)
        self.form.setObjectName(u"form")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.form)


        self.verticalLayout.addLayout(self.formLayout)

        self.find_button = QPushButton(EntitySearch)
        self.find_button.setObjectName(u"find_button")

        self.verticalLayout.addWidget(self.find_button)

        self.entity_list = QListWidget(EntitySearch)
        self.entity_list.setObjectName(u"entity_list")

        self.verticalLayout.addWidget(self.entity_list)


        self.retranslateUi(EntitySearch)

        QMetaObject.connectSlotsByName(EntitySearch)
    # setupUi

    def retranslateUi(self, EntitySearch):
        EntitySearch.setWindowTitle(QCoreApplication.translate("EntitySearch", u"Entity Search", None))
        self.label.setText(QCoreApplication.translate("EntitySearch", u"Type", None))
        self.label_2.setText(QCoreApplication.translate("EntitySearch", u"Subtype", None))
        self.label_3.setText(QCoreApplication.translate("EntitySearch", u"Form", None))
        self.find_button.setText(QCoreApplication.translate("EntitySearch", u"Find", None))
    # retranslateUi

