# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

from mcedit_ui.entity_properties import EntityProperties
from mcedit_ui.room_view import RoomView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 768)
        self.actionLayer_BG1 = QAction(MainWindow)
        self.actionLayer_BG1.setObjectName(u"actionLayer_BG1")
        self.actionLayer_BG1.setCheckable(True)
        self.actionLayer_BG1.setChecked(True)
        self.actionLayer_BG2 = QAction(MainWindow)
        self.actionLayer_BG2.setObjectName(u"actionLayer_BG2")
        self.actionLayer_BG2.setCheckable(True)
        self.actionLayer_BG2.setChecked(True)
        self.actionEntities = QAction(MainWindow)
        self.actionEntities.setObjectName(u"actionEntities")
        self.actionEntities.setCheckable(True)
        self.actionEntities.setChecked(True)
        self.actionTile_Entities = QAction(MainWindow)
        self.actionTile_Entities.setObjectName(u"actionTile_Entities")
        self.actionTile_Entities.setCheckable(True)
        self.actionTile_Entities.setChecked(True)
        self.actionExits = QAction(MainWindow)
        self.actionExits.setObjectName(u"actionExits")
        self.actionExits.setCheckable(True)
        self.actionExits.setChecked(True)
        self.actionEntity_Search = QAction(MainWindow)
        self.actionEntity_Search.setObjectName(u"actionEntity_Search")
        self.actionTest_Room = QAction(MainWindow)
        self.actionTest_Room.setObjectName(u"actionTest_Room")
        self.actionLayer_BG3 = QAction(MainWindow)
        self.actionLayer_BG3.setObjectName(u"actionLayer_BG3")
        self.actionLayer_BG3.setCheckable(True)
        self.actionLayer_BG3.setChecked(True)
        self.actionSave_Editor = QAction(MainWindow)
        self.actionSave_Editor.setObjectName(u"actionSave_Editor")
        self.actionText_Editor = QAction(MainWindow)
        self.actionText_Editor.setObjectName(u"actionText_Editor")
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        self.actionOpen_Project = QAction(MainWindow)
        self.actionOpen_Project.setObjectName(u"actionOpen_Project")
        self.actionSave_Project = QAction(MainWindow)
        self.actionSave_Project.setObjectName(u"actionSave_Project")
        self.actionSave_Project_As = QAction(MainWindow)
        self.actionSave_Project_As.setObjectName(u"actionSave_Project_As")
        self.actionSprite_Editor = QAction(MainWindow)
        self.actionSprite_Editor.setObjectName(u"actionSprite_Editor")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.left_sidebar = QWidget(self.splitter)
        self.left_sidebar.setObjectName(u"left_sidebar")
        self.verticalLayout_2 = QVBoxLayout(self.left_sidebar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.left_sidebar)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.area_index = QComboBox(self.left_sidebar)
        self.area_index.setObjectName(u"area_index")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.area_index)

        self.label_2 = QLabel(self.left_sidebar)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.room_index = QComboBox(self.left_sidebar)
        self.room_index.setObjectName(u"room_index")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.room_index)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.map_graphics_view = QGraphicsView(self.left_sidebar)
        self.map_graphics_view.setObjectName(u"map_graphics_view")

        self.verticalLayout_2.addWidget(self.map_graphics_view)

        self.entity_lists_list = QListWidget(self.left_sidebar)
        self.entity_lists_list.setObjectName(u"entity_lists_list")

        self.verticalLayout_2.addWidget(self.entity_lists_list)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.left_sidebar)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 684, 707))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.room_graphics_view = RoomView(self.scrollAreaWidgetContents)
        self.room_graphics_view.setObjectName(u"room_graphics_view")

        self.verticalLayout.addWidget(self.room_graphics_view)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)
        self.right_sidebar = QTabWidget(self.splitter)
        self.right_sidebar.setObjectName(u"right_sidebar")
        self.right_sidebar.setMinimumSize(QSize(300, 0))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.entity_properies = EntityProperties(self.tab)
        self.entity_properies.setObjectName(u"entity_properies")

        self.verticalLayout_6.addWidget(self.entity_properies)

        self.right_sidebar.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bg2_tileset_graphics_view = QGraphicsView(self.tab_2)
        self.bg2_tileset_graphics_view.setObjectName(u"bg2_tileset_graphics_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bg2_tileset_graphics_view.sizePolicy().hasHeightForWidth())
        self.bg2_tileset_graphics_view.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.bg2_tileset_graphics_view)

        self.right_sidebar.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_8 = QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.bg1_tileset_graphics_view = QGraphicsView(self.tab_3)
        self.bg1_tileset_graphics_view.setObjectName(u"bg1_tileset_graphics_view")

        self.verticalLayout_8.addWidget(self.bg1_tileset_graphics_view)

        self.right_sidebar.addTab(self.tab_3, "")
        self.splitter.addWidget(self.right_sidebar)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuBuild = QMenu(self.menubar)
        self.menuBuild.setObjectName(u"menuBuild")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuBuild.menuAction())
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSave_Project_As)
        self.menuView.addAction(self.actionLayer_BG1)
        self.menuView.addAction(self.actionLayer_BG2)
        self.menuView.addAction(self.actionLayer_BG3)
        self.menuView.addAction(self.actionEntities)
        self.menuView.addAction(self.actionTile_Entities)
        self.menuView.addAction(self.actionExits)
        self.menuTools.addAction(self.actionEntity_Search)
        self.menuTools.addAction(self.actionSave_Editor)
        self.menuTools.addAction(self.actionText_Editor)
        self.menuTools.addAction(self.actionSprite_Editor)
        self.menuBuild.addAction(self.actionTest_Room)
        self.menuEdit.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)

        self.right_sidebar.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minish Cap Editor", None))
        self.actionLayer_BG1.setText(QCoreApplication.translate("MainWindow", u"Layer BG1", None))
        self.actionLayer_BG2.setText(QCoreApplication.translate("MainWindow", u"Layer BG2", None))
        self.actionEntities.setText(QCoreApplication.translate("MainWindow", u"Entities", None))
        self.actionTile_Entities.setText(QCoreApplication.translate("MainWindow", u"Tile Entities", None))
        self.actionExits.setText(QCoreApplication.translate("MainWindow", u"Exits", None))
        self.actionEntity_Search.setText(QCoreApplication.translate("MainWindow", u"Entity Search", None))
#if QT_CONFIG(shortcut)
        self.actionEntity_Search.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionTest_Room.setText(QCoreApplication.translate("MainWindow", u"Test Room", None))
#if QT_CONFIG(shortcut)
        self.actionTest_Room.setShortcut(QCoreApplication.translate("MainWindow", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.actionLayer_BG3.setText(QCoreApplication.translate("MainWindow", u"Layer BG3", None))
        self.actionSave_Editor.setText(QCoreApplication.translate("MainWindow", u"Save Editor", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Editor.setShortcut(QCoreApplication.translate("MainWindow", u"V", None))
#endif // QT_CONFIG(shortcut)
        self.actionText_Editor.setText(QCoreApplication.translate("MainWindow", u"Text Editor", None))
#if QT_CONFIG(shortcut)
        self.actionText_Editor.setShortcut(QCoreApplication.translate("MainWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionOpen_Project.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.actionSave_Project.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.actionSave_Project_As.setText(QCoreApplication.translate("MainWindow", u"Save Project As", None))
        self.actionSprite_Editor.setText(QCoreApplication.translate("MainWindow", u"Sprite Editor", None))
#if QT_CONFIG(shortcut)
        self.actionSprite_Editor.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Room", None))
        self.right_sidebar.setTabText(self.right_sidebar.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Entities", None))
        self.right_sidebar.setTabText(self.right_sidebar.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"BG2", None))
        self.right_sidebar.setTabText(self.right_sidebar.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"BG1", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuBuild.setTitle(QCoreApplication.translate("MainWindow", u"Build", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

