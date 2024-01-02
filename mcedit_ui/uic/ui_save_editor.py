# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGridLayout, QHBoxLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SaveEditor(object):
    def setupUi(self, SaveEditor):
        if not SaveEditor.objectName():
            SaveEditor.setObjectName(u"SaveEditor")
        SaveEditor.resize(1024, 720)
        self.verticalLayout = QVBoxLayout(SaveEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.import_raw_save = QPushButton(SaveEditor)
        self.import_raw_save.setObjectName(u"import_raw_save")

        self.horizontalLayout.addWidget(self.import_raw_save)

        self.import_vba_mgba_save = QPushButton(SaveEditor)
        self.import_vba_mgba_save.setObjectName(u"import_vba_mgba_save")

        self.horizontalLayout.addWidget(self.import_vba_mgba_save)

        self.import_gameshark_save = QPushButton(SaveEditor)
        self.import_gameshark_save.setObjectName(u"import_gameshark_save")

        self.horizontalLayout.addWidget(self.import_gameshark_save)

        self.export_raw_save = QPushButton(SaveEditor)
        self.export_raw_save.setObjectName(u"export_raw_save")

        self.horizontalLayout.addWidget(self.export_raw_save)

        self.export_vba_mgba_save = QPushButton(SaveEditor)
        self.export_vba_mgba_save.setObjectName(u"export_vba_mgba_save")

        self.horizontalLayout.addWidget(self.export_vba_mgba_save)

        self.export_gameshark_save = QPushButton(SaveEditor)
        self.export_gameshark_save.setObjectName(u"export_gameshark_save")

        self.horizontalLayout.addWidget(self.export_gameshark_save)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selected_slot_index = QComboBox(SaveEditor)
        self.selected_slot_index.addItem("")
        self.selected_slot_index.addItem("")
        self.selected_slot_index.addItem("")
        self.selected_slot_index.setObjectName(u"selected_slot_index")
        self.selected_slot_index.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.selected_slot_index)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(SaveEditor)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1000, 628))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.owned_figurines_layout = QVBoxLayout()
        self.owned_figurines_layout.setObjectName(u"owned_figurines_layout")

        self.horizontalLayout_3.addLayout(self.owned_figurines_layout)

        self.owned_items_layout = QFormLayout()
        self.owned_items_layout.setObjectName(u"owned_items_layout")

        self.horizontalLayout_3.addLayout(self.owned_items_layout)

        self.flags_layout = QGridLayout()
        self.flags_layout.setObjectName(u"flags_layout")

        self.horizontalLayout_3.addLayout(self.flags_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(SaveEditor)

        QMetaObject.connectSlotsByName(SaveEditor)
    # setupUi

    def retranslateUi(self, SaveEditor):
        SaveEditor.setWindowTitle(QCoreApplication.translate("SaveEditor", u"Save Editor", None))
        self.import_raw_save.setText(QCoreApplication.translate("SaveEditor", u"Import Raw Save", None))
        self.import_vba_mgba_save.setText(QCoreApplication.translate("SaveEditor", u"Import VBA/mGBA Save", None))
        self.import_gameshark_save.setText(QCoreApplication.translate("SaveEditor", u"Import GameShark Save", None))
        self.export_raw_save.setText(QCoreApplication.translate("SaveEditor", u"Export Raw Save", None))
        self.export_vba_mgba_save.setText(QCoreApplication.translate("SaveEditor", u"Export VBA/mGBA Save", None))
        self.export_gameshark_save.setText(QCoreApplication.translate("SaveEditor", u"Export GameShark Save", None))
        self.selected_slot_index.setItemText(0, QCoreApplication.translate("SaveEditor", u"Save Slot 1", None))
        self.selected_slot_index.setItemText(1, QCoreApplication.translate("SaveEditor", u"Save Slot 2", None))
        self.selected_slot_index.setItemText(2, QCoreApplication.translate("SaveEditor", u"Save Slot 3", None))

    # retranslateUi

