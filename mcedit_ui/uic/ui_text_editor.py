# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_editor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_TextEditor(object):
    def setupUi(self, TextEditor):
        if not TextEditor.objectName():
            TextEditor.setObjectName(u"TextEditor")
        TextEditor.resize(1024, 720)
        self.verticalLayout = QVBoxLayout(TextEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.message_group_index = QComboBox(TextEditor)
        self.message_group_index.setObjectName(u"message_group_index")

        self.horizontalLayout_2.addWidget(self.message_group_index)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.message_list = QListWidget(TextEditor)
        self.message_list.setObjectName(u"message_list")
        self.message_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout.addWidget(self.message_list)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(TextEditor)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.rom_location = QLineEdit(TextEditor)
        self.rom_location.setObjectName(u"rom_location")
        self.rom_location.setMaximumSize(QSize(80, 16777215))
        self.rom_location.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.rom_location)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.message_text_edit = QTextEdit(TextEditor)
        self.message_text_edit.setObjectName(u"message_text_edit")

        self.verticalLayout_2.addWidget(self.message_text_edit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(TextEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TextEditor)
        self.buttonBox.accepted.connect(TextEditor.accept)
        self.buttonBox.rejected.connect(TextEditor.reject)

        QMetaObject.connectSlotsByName(TextEditor)
    # setupUi

    def retranslateUi(self, TextEditor):
        TextEditor.setWindowTitle(QCoreApplication.translate("TextEditor", u"Text Editor", None))
        self.label.setText(QCoreApplication.translate("TextEditor", u"ROM Location", None))
    # retranslateUi

