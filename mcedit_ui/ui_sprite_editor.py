# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sprite_editor.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SpriteEditor(object):
    def setupUi(self, SpriteEditor):
        if SpriteEditor.objectName():
            SpriteEditor.setObjectName(u"SpriteEditor")
        SpriteEditor.resize(832, 478)
        self.verticalLayout = QVBoxLayout(SpriteEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(SpriteEditor)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.enemy_list = QListWidget(self.tab)
        self.enemy_list.setObjectName(u"enemy_list")

        self.verticalLayout_3.addWidget(self.enemy_list)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.object_list = QListWidget(self.tab_2)
        self.object_list.setObjectName(u"object_list")

        self.verticalLayout_4.addWidget(self.object_list)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.npc_list = QListWidget(self.tab_3)
        self.npc_list.setObjectName(u"npc_list")

        self.verticalLayout_5.addWidget(self.npc_list)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.player_list = QListWidget(self.tab_4)
        self.player_list.setObjectName(u"player_list")

        self.verticalLayout_6.addWidget(self.player_list)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.type_4s_list = QListWidget(self.tab_5)
        self.type_4s_list.setObjectName(u"type_4s_list")

        self.verticalLayout_7.addWidget(self.type_4s_list)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_8 = QVBoxLayout(self.tab_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.player_items_list = QListWidget(self.tab_6)
        self.player_items_list.setObjectName(u"player_items_list")

        self.verticalLayout_8.addWidget(self.player_items_list)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(SpriteEditor)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.form_index = QComboBox(SpriteEditor)
        self.form_index.setObjectName(u"form_index")

        self.horizontalLayout_2.addWidget(self.form_index)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(SpriteEditor)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.anim_index = QComboBox(SpriteEditor)
        self.anim_index.setObjectName(u"anim_index")

        self.horizontalLayout_3.addWidget(self.anim_index)

        self.label_2 = QLabel(SpriteEditor)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.frame_index = QComboBox(SpriteEditor)
        self.frame_index.setObjectName(u"frame_index")

        self.horizontalLayout_3.addWidget(self.frame_index)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_9)

        self.sprite_graphics_view = QGraphicsView(SpriteEditor)
        self.sprite_graphics_view.setObjectName(u"sprite_graphics_view")

        self.verticalLayout_2.addWidget(self.sprite_graphics_view)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(SpriteEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SpriteEditor)
        self.buttonBox.accepted.connect(SpriteEditor.accept)
        self.buttonBox.rejected.connect(SpriteEditor.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpriteEditor)
    # setupUi

    def retranslateUi(self, SpriteEditor):
        SpriteEditor.setWindowTitle(QCoreApplication.translate("SpriteEditor", u"Text Editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SpriteEditor", u"Enemies", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SpriteEditor", u"Objects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SpriteEditor", u"NPCs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("SpriteEditor", u"Player", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("SpriteEditor", u"Type 4s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("SpriteEditor", u"Player Items", None))
        self.label_3.setText(QCoreApplication.translate("SpriteEditor", u"Form", None))
        self.label.setText(QCoreApplication.translate("SpriteEditor", u"Animation", None))
        self.label_2.setText(QCoreApplication.translate("SpriteEditor", u"Frame", None))
    # retranslateUi

