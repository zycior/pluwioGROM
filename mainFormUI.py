# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created: Sat Jan 19 21:03:01 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(770, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/dodatkowe/IKONY/32x32/lightning.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setMinimumSize(QtCore.QSize(50, 0))
        self.listWidget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.metadataTable = QtGui.QTableWidget(self.centralwidget)
        self.metadataTable.setMinimumSize(QtCore.QSize(0, 300))
        self.metadataTable.setMaximumSize(QtCore.QSize(16777215, 483))
        self.metadataTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.metadataTable.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.SelectedClicked)
        self.metadataTable.setAlternatingRowColors(True)
        self.metadataTable.setRowCount(15)
        self.metadataTable.setColumnCount(2)
        self.metadataTable.setObjectName(_fromUtf8("metadataTable"))
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.metadataTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(7, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(8, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(9, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(10, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(11, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(12, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable)
        self.metadataTable.setItem(13, 0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.metadataTable.setItem(14, 0, item)
        self.metadataTable.horizontalHeader().setVisible(False)
        self.metadataTable.horizontalHeader().setDefaultSectionSize(200)
        self.metadataTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.metadataTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.Picture = QtGui.QScrollArea(self.centralwidget)
        self.Picture.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px;"))
        self.Picture.setWidgetResizable(True)
        self.Picture.setObjectName(_fromUtf8("Picture"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 750, 148))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pic_lab = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pic_lab.setText(_fromUtf8(""))
        self.pic_lab.setObjectName(_fromUtf8("pic_lab"))
        self.horizontalLayout_3.addWidget(self.pic_lab)
        self.Picture.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.Picture)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuPlik = QtGui.QMenu(self.menubar)
        self.menuPlik.setObjectName(_fromUtf8("menuPlik"))
        self.menuPomoc = QtGui.QMenu(self.menubar)
        self.menuPomoc.setObjectName(_fromUtf8("menuPomoc"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setCheckable(False)
        self.actionNew.setChecked(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/baza danych/Nowa baza danych")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/baza danych/Otwórz bazę danych")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionO_programie = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/dodatkowe/IKONY/32x32/information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionO_programie.setIcon(icon3)
        self.actionO_programie.setObjectName(_fromUtf8("actionO_programie"))
        self.actionAddPluw = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/dane/IKONY/32x32/page_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddPluw.setIcon(icon4)
        self.actionAddPluw.setObjectName(_fromUtf8("actionAddPluw"))
        self.actionDelPluw = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/dane/IKONY/32x32/page_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelPluw.setIcon(icon5)
        self.actionDelPluw.setObjectName(_fromUtf8("actionDelPluw"))
        self.actionAddGroup = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/dane/IKONY/32x32/folder_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddGroup.setIcon(icon6)
        self.actionAddGroup.setObjectName(_fromUtf8("actionAddGroup"))
        self.menuPlik.addAction(self.actionNew)
        self.menuPlik.addAction(self.actionOpen)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionExit)
        self.menuPomoc.addAction(self.actionO_programie)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddGroup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddPluw)
        self.toolBar.addAction(self.actionDelPluw)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PluwioGROM", None))
        self.label.setText(_translate("MainWindow", "Lokalizacja:", None))
        self.listWidget.setSortingEnabled(True)
        self.label_3.setText(_translate("MainWindow", "Data pomiaru:", None))
        self.label_2.setText(_translate("MainWindow", "Metadane:", None))
        __sortingEnabled = self.metadataTable.isSortingEnabled()
        self.metadataTable.setSortingEnabled(False)
        item = self.metadataTable.item(0, 0)
        item.setText(_translate("MainWindow", "Mierzony parametr", None))
        item = self.metadataTable.item(1, 0)
        item.setText(_translate("MainWindow", "Przyrząd pomiarowy", None))
        item = self.metadataTable.item(2, 0)
        item.setText(_translate("MainWindow", "Metoda pomiaru", None))
        item = self.metadataTable.item(3, 0)
        item.setText(_translate("MainWindow", "Rodzaj zapisu danych", None))
        item = self.metadataTable.item(4, 0)
        item.setText(_translate("MainWindow", "Cechy wykresu", None))
        item = self.metadataTable.item(5, 0)
        item.setText(_translate("MainWindow", "Jednostka pomiarowa", None))
        item = self.metadataTable.item(6, 0)
        item.setText(_translate("MainWindow", "Dokładność pomiarowa", None))
        item = self.metadataTable.item(7, 0)
        item.setText(_translate("MainWindow", "Skala pomiaru", None))
        item = self.metadataTable.item(8, 0)
        item.setText(_translate("MainWindow", "Lokalizacja", None))
        item = self.metadataTable.item(9, 0)
        item.setText(_translate("MainWindow", "Miejsce", None))
        item = self.metadataTable.item(10, 0)
        item.setText(_translate("MainWindow", "Obserwator", None))
        item = self.metadataTable.item(11, 0)
        item.setText(_translate("MainWindow", "Badane lata", None))
        item = self.metadataTable.item(12, 0)
        item.setText(_translate("MainWindow", "Częstotliwość pomiaru", None))
        item = self.metadataTable.item(13, 0)
        item.setText(_translate("MainWindow", "Stacja pomiarowa", None))
        item = self.metadataTable.item(14, 0)
        item.setText(_translate("MainWindow", "Uwagi", None))
        self.metadataTable.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Pasek pluwiogramu:", None))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik", None))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNew.setText(_translate("MainWindow", "Nowa baza", None))
        self.actionNew.setStatusTip(_translate("MainWindow", "Tworzy nową bazę danych.", None))
        self.actionOpen.setText(_translate("MainWindow", "Otwórz bazę", None))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Otwiera istniejący plik bazy danych.", None))
        self.actionExit.setText(_translate("MainWindow", "Wyjście", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Kończy działanie programu.", None))
        self.actionO_programie.setText(_translate("MainWindow", "O programie...", None))
        self.actionO_programie.setStatusTip(_translate("MainWindow", "Informacje o programie.", None))
        self.actionAddPluw.setText(_translate("MainWindow", "Dodaj pluwiogram", None))
        self.actionAddPluw.setIconText(_translate("MainWindow", "Dodaj pomiar", None))
        self.actionAddPluw.setToolTip(_translate("MainWindow", "Dodaj pomiar", None))
        self.actionAddPluw.setStatusTip(_translate("MainWindow", "Tworzy nowy pomiar powiązany z aktualnie wybranym zbiorem", None))
        self.actionDelPluw.setText(_translate("MainWindow", "Usuń pluwiogram", None))
        self.actionDelPluw.setIconText(_translate("MainWindow", "Usuń pomiar", None))
        self.actionDelPluw.setToolTip(_translate("MainWindow", "Usuń pomiar", None))
        self.actionDelPluw.setStatusTip(_translate("MainWindow", "Usuwa wybrany pomiar ze zbioru", None))
        self.actionAddGroup.setText(_translate("MainWindow", "Dodaj zbiór pomiarów", None))
        self.actionAddGroup.setToolTip(_translate("MainWindow", "Dodaj zbiór pomiarów", None))
        self.actionAddGroup.setStatusTip(_translate("MainWindow", "Tworzy nowy wpis metadanych dla zbioru pomiarów", None))

import resources_rc