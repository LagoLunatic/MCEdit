# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(600, 200)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.emulator_path = QLineEdit(Settings)
        self.emulator_path.setObjectName(u"emulator_path")

        self.gridLayout.addWidget(self.emulator_path, 0, 1, 1, 1)

        self.emulator_path_browse_button = QPushButton(Settings)
        self.emulator_path_browse_button.setObjectName(u"emulator_path_browse_button")

        self.gridLayout.addWidget(self.emulator_path_browse_button, 0, 2, 1, 1)

        self.label_2 = QLabel(Settings)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.test_room_save_slot = QComboBox(Settings)
        self.test_room_save_slot.setObjectName(u"test_room_save_slot")
        self.test_room_save_slot.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.test_room_save_slot, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Entity Search", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Test Room Emulator Path", None))
        self.emulator_path_browse_button.setText(QCoreApplication.translate("Settings", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Test Room Save Slot", None))
    # retranslateUi

