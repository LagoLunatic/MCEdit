# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Thu Mar 14 14:09:22 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.area_index = QtWidgets.QComboBox(self.centralwidget)
        self.area_index.setObjectName("area_index")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.area_index)
        self.room_index = QtWidgets.QComboBox(self.centralwidget)
        self.room_index.setObjectName("room_index")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.room_index)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.map_graphics_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.map_graphics_view.setMaximumSize(QtCore.QSize(300, 1024))
        self.map_graphics_view.setObjectName("map_graphics_view")
        self.verticalLayout_2.addWidget(self.map_graphics_view)
        self.entity_lists_list = QtWidgets.QListWidget(self.centralwidget)
        self.entity_lists_list.setMinimumSize(QtCore.QSize(300, 0))
        self.entity_lists_list.setMaximumSize(QtCore.QSize(300, 16777215))
        self.entity_lists_list.setObjectName("entity_lists_list")
        self.verticalLayout_2.addWidget(self.entity_lists_list)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 578, 693))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.room_graphics_view = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.room_graphics_view.setObjectName("room_graphics_view")
        self.verticalLayout.addWidget(self.room_graphics_view)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.entity_properies = EntityProperties(self.centralwidget)
        self.entity_properies.setMinimumSize(QtCore.QSize(360, 0))
        self.entity_properies.setMaximumSize(QtCore.QSize(360, 16777215))
        self.entity_properies.setObjectName("entity_properies")
        self.verticalLayout_3.addWidget(self.entity_properies)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_ROM = QtWidgets.QAction(MainWindow)
        self.actionOpen_ROM.setObjectName("actionOpen_ROM")
        self.actionLayer_BG1 = QtWidgets.QAction(MainWindow)
        self.actionLayer_BG1.setCheckable(True)
        self.actionLayer_BG1.setChecked(True)
        self.actionLayer_BG1.setObjectName("actionLayer_BG1")
        self.actionLayer_BG2 = QtWidgets.QAction(MainWindow)
        self.actionLayer_BG2.setCheckable(True)
        self.actionLayer_BG2.setChecked(True)
        self.actionLayer_BG2.setObjectName("actionLayer_BG2")
        self.actionEntities = QtWidgets.QAction(MainWindow)
        self.actionEntities.setCheckable(True)
        self.actionEntities.setChecked(True)
        self.actionEntities.setObjectName("actionEntities")
        self.actionTile_Entities = QtWidgets.QAction(MainWindow)
        self.actionTile_Entities.setCheckable(True)
        self.actionTile_Entities.setChecked(True)
        self.actionTile_Entities.setObjectName("actionTile_Entities")
        self.actionExits = QtWidgets.QAction(MainWindow)
        self.actionExits.setCheckable(True)
        self.actionExits.setChecked(True)
        self.actionExits.setObjectName("actionExits")
        self.menuFile.addAction(self.actionOpen_ROM)
        self.menuView.addAction(self.actionLayer_BG1)
        self.menuView.addAction(self.actionLayer_BG2)
        self.menuView.addAction(self.actionEntities)
        self.menuView.addAction(self.actionTile_Entities)
        self.menuView.addAction(self.actionExits)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Minish Cap Editor", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Area", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Room", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("MainWindow", "View", None, -1))
        self.actionOpen_ROM.setText(QtWidgets.QApplication.translate("MainWindow", "Open ROM", None, -1))
        self.actionLayer_BG1.setText(QtWidgets.QApplication.translate("MainWindow", "Layer BG1", None, -1))
        self.actionLayer_BG2.setText(QtWidgets.QApplication.translate("MainWindow", "Layer BG2", None, -1))
        self.actionEntities.setText(QtWidgets.QApplication.translate("MainWindow", "Entities", None, -1))
        self.actionTile_Entities.setText(QtWidgets.QApplication.translate("MainWindow", "Tile Entities", None, -1))
        self.actionExits.setText(QtWidgets.QApplication.translate("MainWindow", "Exits", None, -1))

from mcedit_ui.entity_properties import EntityProperties
