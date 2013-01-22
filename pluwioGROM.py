# -*- coding: utf-8 -*-

import sys
import os
#from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from mainFormUI import Ui_MainWindow
from addForm import addDialog
from aboutUI import Ui_aboutDialog

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
	
		#ustawianie interfejsu z QtDesignera
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("PluwioGROM [brak bazy]")
		
		#-----------------------------------------------------
		self.stacjaPomiarowaCombo = QComboBox()
		self.stacjaPomiarowaCombo.addItem("Czynna")
		self.stacjaPomiarowaCombo.addItem("Nieczynna")
		
		self.metodaPomiaruCombo = QComboBox()
		self.metodaPomiaruCombo.addItem("Automatyczna")
		self.metodaPomiaruCombo.addItem("Tradycyjna")
		
		self.rodzajZapisuDanychCombo = QComboBox()
		self.rodzajZapisuDanychCombo.addItem("Dziennik")
		self.rodzajZapisuDanychCombo.addItem("Samopis analogowy")
		self.rodzajZapisuDanychCombo.addItem("Samopis cyfrowy")
		#-----------------------------------------------------
		
		self.ui.metadataTable.setCellWidget(13, 1, self.stacjaPomiarowaCombo)
		self.ui.metadataTable.setCellWidget(2, 1, self.metodaPomiaruCombo)
		self.ui.metadataTable.setCellWidget(3, 1, self.rodzajZapisuDanychCombo)
		
		#ustawienia bazy danych
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.query = QSqlQuery(self.db)
		
		#tworzenie okien pomocniczych
		self.addDialog = addDialog()
		
		#zmienne pomocnicze
		self.selectedID = -1
		self.disableCellChanged = False
		self.image = QImage()
		
		self.lokalizacja = []
		self.pluwiogram = []
		
		#tworzenie polaczen
		self.ui.actionExit.triggered.connect(qApp.quit)
		self.ui.actionNew.triggered.connect(self.createNewDB)
		self.ui.actionOpen.triggered.connect(self.openDB)
		self.ui.actionAddPluw.triggered.connect(self.addEntry)
		self.ui.actionDelPluw.triggered.connect(self.delEntry)
		self.ui.actionAddGroup.triggered.connect(self.addGroup)
		self.ui.actionO_programie.triggered.connect(self.about)
		#self.ui.listWidget.itemSelectionChanged.connect(self.groupSelChanged)
		self.connect(self.ui.listWidget, SIGNAL("currentRowChanged(int)"), self.groupSelChanged)
		self.connect(self.ui.listWidget_2, SIGNAL("currentRowChanged(int)"), self.entrySelChanged)
		self.connect(self.ui.metadataTable, SIGNAL("cellChanged(int, int)"), self.rowChanged)
		
		self.connect(self.stacjaPomiarowaCombo, SIGNAL("currentIndexChanged(int)"), self.rowStacjaPomiarowaChanged)
		self.connect(self.metodaPomiaruCombo, SIGNAL("currentIndexChanged(int)"), self.rowMetodaPomiaruComboChanged)
		self.connect(self.rodzajZapisuDanychCombo, SIGNAL("currentIndexChanged(int)"), self.rowRodzajZapisuDanychChanged)

		
		self.blockFunctionality()
		
		self.show()

	def blockFunctionality(self):		# blokuje u¿ycie funkcjonalnosci programu - stan przed wczytaniem bazy danych lub w przypadku niepowodzenia przy wczytywaniu
		self.ui.metadataTable.setEnabled(False)
		self.ui.actionAddPluw.setEnabled(False)
		self.ui.actionDelPluw.setEnabled(False)
		self.ui.actionAddGroup.setEnabled(False)
		self.clearMetadata()
		self.ui.listWidget.clear()
		self.ui.listWidget_2.clear()
		
	def createNewDB(self):				# tworzenie nowego pliku bazy danych
		path = QFileDialog.getSaveFileName(self,"Nowy plik", ".","Pliki programu PluwioGROM (*.dbp)")
		
		if path == "":
			return
		
		self.setWindowTitle("PluwioGROM [brak bazy]")
		self.blockFunctionality()
		
		if path.endswith('.dbp') == False:	# jezeli niezgodne rozszerzenie pliku - poprawiamy 
			path = path + ".dbp"
		
		file_info = QFileInfo(path)
		if file_info.exists() == True:
			file = QFile(path)
			if file.remove() == False:
				QMessageBox.critical(self, "Blad", "Nie mozna usunac pliku: " + path, QMessageBox.Ok, QMessageBox.Ok)
				return
		
		if self.db.isOpen():
			self.db.close()
		
		self.db.setDatabaseName(path)
		self.db.open()
		
		if self.db.isOpen:
			lQuery = QSqlQuery()
			
			query_result = lQuery.exec_('CREATE TABLE Metadane (ID_Metadane INTEGER PRIMARY KEY AUTOINCREMENT, ' \
				'Mierzony_parametr TEXT, Przyrzad_pomiarowy TEXT, Metoda_pomiaru TEXT, Rodzaj_zapisu_danych TEXT, Cechy_wykresu_danych TEXT, '\
				'Jednostka_pomiarowa TEXT, Dokladnosc_pomiarowa TEXT, Skala_pomiaru TEXT, Lokalizacja TEXT, Miejsce TEXT, Obserwator TEXT, '\
				'Czestotliwosc_pomiaru TEXT, Stacja_pomiarowa TEXT, Uwagi TEXT)')
			
			if query_result == False:
				QMessageBox.critical(self, "Blad", "Niepowodzenie przy tworzeniu zbioru:" + path, QMessageBox.Ok, QMessageBox.Ok)
				return
			
			query_result = lQuery.exec_('CREATE TABLE Pluwiogram (ID INTEGER PRIMARY KEY AUTOINCREMENT, ID_Metadane INTEGER, Data TEXT, Sciezka TEXT)')
			
			if query_result == False:
				QMessageBox.critical(self, "Blad", "Niepowodzenie przy tworzeniu zbioru:" + path, QMessageBox.Ok, QMessageBox.Ok)
				return
			else:
				self.setWindowTitle("PluwioGROM ["+path+"]")
				
			self.ui.actionAddGroup.setEnabled(True)
			
		else:
			QMessageBox.critical(self, "Blad", "Niepowodzenie przy tworzeniu zbioru:" + path, QMessageBox.Ok, QMessageBox.Ok)
		
		
	def openDB(self):		# otwieranie istniejacego pliku bazy danych
		path = QFileDialog.getOpenFileName(self,"Otworz plik", ".","Pliki programu PluwioGROM (*.dbp)")	
		
		if path == "":
			return
		
		self.blockFunctionality()
		self.setWindowTitle("PluwioGROM [brak bazy]")
		
		if self.db.isOpen():
			self.db.close()
		
		self.db.setDatabaseName(path)
		
		self.ui.listWidget.clear()
		self.ui.listWidget_2.clear()
		self.db.open()
		
		if self.db.isOpen():
			self.setWindowTitle("PluwioGROM ["+path+"]")
			self.getLocalisationFromDB()
				
			self.ui.actionAddGroup.setEnabled(True)
		else:
			self.setWindowTitle("PluwioGROM! [brak bazy]")
			QMessageBox.critical(self, "Blad", "Podany plik:" + path + " nie jest poprawna baza danych.", QMessageBox.Ok, QMessageBox.Ok)
	
	def addEntry(self):
		values = []
		index = 0
		for i in range(0, 15):
			if i==2:
				values.append(self.metodaPomiaruCombo.currentIndex())
			elif i==3:
				values.append(self.rodzajZapisuDanychCombo.currentIndex())
			elif i==13:
				values.append(self.stacjaPomiarowaCombo.currentIndex())
			elif i!=11:
				values.append(self.ui.metadataTable.item(index, 1).text())
			index = index+1
						
		self.addDialog.prepareToShow(values)
		self.addDialog.ui.groupBox.setEnabled(False)
		self.addDialog.ui.groupBox_2.setEnabled(True)
		self.addDialog.metadataApplied()
		self.addDialog.exec_()
		if self.addDialog.result() == QDialog.Accepted:
			self.ui.listWidget_2.clear()
			self.pluwiogram = []
	
	def delEntry(self):
		result = QMessageBox.question(self, "Usun pluwiogram", "Czy na pewno chcesz usunac wybrany pluwiogram?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if result == QMessageBox.Yes:
			index = self.ui.listWidget_2.currentRow()
			self.ui.listWidget_2.setCurrentRow(-1)
			ID_Metadane = self.pluwiogram[index][2]
			self.query.exec_("DELETE FROM Pluwiogram WHERE ID = " + str(self.pluwiogram[index][3]))
			self.query = QSqlQuery("SELECT count(ID) FROM Pluwiogram WHERE Sciezka='"+self.pluwiogram[index][1]+"'")
			if self.query.next():
				if int(self.query.value(0)) == 0:
					try:
						os.remove(self.pluwiogram[index][1])
					except OSError:
						QMessageBox.critical(self, "Blad", "Proba usuniecia pliku pluwiogramu zakonczyla sie niepowodzeniem!", QMessageBox.Ok, QMessageBox.Ok)
			del self.pluwiogram[index]
			self.ui.listWidget_2.takeItem(index)
			self.query = QSqlQuery("SELECT count(ID_Metadane) FROM Pluwiogram WHERE ID_Metadane="+str(ID_Metadane))
			if self.query.next():
					count = int(self.query.value(0))
					if count == 0:
						self.query.exec_("DELETE FROM Metadane WHERE ID_Metadane = "+str(ID_Metadane))
						self.ui.listWidget.setCurrentRow(-1)
						self.getLocalisationFromDB()
			
	def addGroup(self):
		values = []
		index = 0
		for i in range(0, 15):
			if i==2:
				values.append(self.metodaPomiaruCombo.currentIndex())
			elif i==3:
				values.append(self.rodzajZapisuDanychCombo.currentIndex())
			elif i==13:
				values.append(self.stacjaPomiarowaCombo.currentIndex())
			elif i!=11:
				values.append(self.ui.metadataTable.item(index, 1).text())
			index = index+1
						
		self.addDialog.prepareToShow(values)
		self.addDialog.exec_()
		if self.addDialog.result() == QDialog.Accepted:
			self.ui.listWidget.setCurrentRow(-1)
			self.ui.listWidget_2.setCurrentRow(-1)
			self.getLocalisationFromDB()
			self.ui.listWidget_2.clear()
			self.pluwiogram = []
			index = self.ui.listWidget.currentRow()
			self.query = QSqlQuery("SELECT Data, Sciezka, Pluwiogram.ID_Metadane, ID FROM Pluwiogram, Metadane WHERE Pluwiogram.ID_Metadane = Metadane.ID_Metadane AND Lokalizacja = '" + self.lokalizacja[index][0] + "' AND Miejsce='" + self.lokalizacja[index][1] + "' ORDER BY Data")
			while self.query.next():
				self.pluwiogram.append( [self.query.value(0), self.query.value(1), self.query.value(2), self.query.value(3)] )
				self.ui.listWidget_2.addItem(self.query.value(0))
	
	def groupSelChanged(self, index):
		self.disabledCellChanged = True
		self.ui.listWidget_2.setCurrentRow(-1)
		self.query = QSqlQuery("SELECT Data, Sciezka, Pluwiogram.ID_Metadane, ID FROM Pluwiogram, Metadane WHERE Pluwiogram.ID_Metadane = Metadane.ID_Metadane AND Lokalizacja = '" + self.lokalizacja[index][0] + "' AND Miejsce='" + self.lokalizacja[index][1] + "' ORDER BY Data")
		self.pluwiogram = []
		while self.query.next():
			self.pluwiogram.append( [self.query.value(0), self.query.value(1), self.query.value(2), self.query.value(3)] )

		self.ui.listWidget_2.clear()
		for i in self.pluwiogram:
			self.ui.listWidget_2.addItem(i[0])
		self.disabledCellChanged = False
		self.ui.pic_lab.setPixmap(QPixmap())
		
	def entrySelChanged(self, index):
		self.ui.actionDelPluw.setEnabled(index != -1)
		self.ui.metadataTable.setEnabled(index != -1)
		self.ui.actionAddPluw.setEnabled(index != -1)
		
		self.clearMetadata()
		self.selectedID = -1
		if index == -1 or self.ui.listWidget_2.count() == 0:
			return
			
		self.query = QSqlQuery("SELECT Mierzony_parametr, Przyrzad_pomiarowy, Metoda_pomiaru, "\
"Rodzaj_zapisu_danych, Cechy_wykresu_danych, Jednostka_pomiarowa, Dokladnosc_pomiarowa, "\
"Skala_pomiaru, Lokalizacja, Miejsce, Obserwator, ID_Metadane, Czestotliwosc_pomiaru, "\
"Stacja_pomiarowa, Uwagi FROM Metadane WHERE ID_Metadane = "+str(self.pluwiogram[index][2]))
		if self.query.next():
			i = 0
			self.ui.metadataTable.setEnabled(True)
			while i < 15:
				if i != 11:
					value = self.query.value(i)
				else: # wyznaczamy badane lata
					aux_query = QSqlQuery("SELECT strftime('%Y',min(Data)), strftime('%Y', max(Data)) from Pluwiogram WHERE ID_Metadane = " + str(self.pluwiogram[index][2]))
					value = ""
					if aux_query.next():
						value = aux_query.value(0) + "-" + aux_query.value(1)
				self.disableRowChanged = True
				
				if type(value) == type('str'):
					item = QTableWidgetItem()
					item.setText(value)
					if i == 8 or i == 9 or i == 11:
						item.setFlags( Qt.ItemIsSelectable ) 
					if i == 2: # metoda pomiaru
						if value == "Automat":
							self.metodaPomiaruCombo.setCurrentIndex(0)
						else:
							self.metodaPomiaruCombo.setCurrentIndex(1)
					elif i == 3:	# rodzaj zapisu danych
						if value == "Dziennik":
							self.rodzajZapisuDanychCombo.setCurrentIndex(0)
						elif value == "Samopis analogowy":
							self.rodzajZapisuDanychCombo.setCurrentIndex(1)
						else:
							self.rodzajZapisuDanychCombo.setCurrentIndex(2)
					elif i == 13: # stacja pomiarowa
						if value == "Czynna":
							self.stacjaPomiarowaCombo.setCurrentIndex(0)
						else:
							self.stacjaPomiarowaCombo.setCurrentIndex(1)
					else:
						self.ui.metadataTable.setItem(i, 1, item)
				else:
					self.ui.metadataTable.setItem(i, 1, QTableWidgetItem())
				self.disableRowChanged = False
				i = i + 1
		self.selectedID = self.pluwiogram[index][2]
		self.image = QImage(self.pluwiogram[index][1])
		self.ui.pic_lab.setPixmap(QPixmap.fromImage(self.image.scaledToHeight(self.ui.pic_lab.height())))
		
		
			
	def rowChanged(self, row, col):
		if self.disabledCellChanged or self.selectedID == -1:
			return
		
		columns = ["Mierzony_parametr", "Przyrzad_pomiarowy", "Metoda_pomiaru", "Rodzaj_zapisu_danych", 
		"Cechy_wykresu_danych", "Jednostka_pomiarowa", "Dokladnosc_pomiarowa", "Skala_pomiaru",
		"Lokalizacja", "Miejsce", "Obserwator", "Badane_lata", "Czestotliwosc_pomiaru", "Stacja_pomiarowa", "Uwagi"]
		
		res = self.query.exec_("UPDATE Metadane SET " + columns[row] + " = '" + self.ui.metadataTable.item(row, col).text() + "' WHERE ID_Metadane = " + str(self.selectedID))
	
		if res == False:
			QMessageBox.warning(self, "Blad", "Nie mozna wykonac polecenia SQL dla obecnej bazy danych!", QMessageBox.Ok, QMessageBox.Ok)

	def rowStacjaPomiarowaChanged(self):
		if self.disabledCellChanged or self.selectedID == -1:
			return
		
		value = self.stacjaPomiarowaCombo.currentText()
		res = self.query.exec_("UPDATE Metadane SET Stacja_pomiarowa = '" + value + "' WHERE ID_Metadane = " + str(self.selectedID))
		if res == False:
			QMessageBox.warning(self, "Blad", "Nie mozna wykonac polecenia SQL dla obecnej bazy danych!", QMessageBox.Ok, QMessageBox.Ok)

		
			
	def rowMetodaPomiaruComboChanged(self):
		if self.disabledCellChanged or self.selectedID == -1:
			return
		value = self.metodaPomiaruCombo.currentText()
		res = self.query.exec_("UPDATE Metadane SET Metoda_pomiaru = '" + value + "' WHERE ID_Metadane = " + str(self.selectedID))
		if res == False:
			QMessageBox.warning(self, "Blad", "Nie mozna wykonac polecenia SQL dla obecnej bazy danych!", QMessageBox.Ok, QMessageBox.Ok)

	def rowRodzajZapisuDanychChanged(self):
		if self.disabledCellChanged or self.selectedID == -1:
			return
		value = self.rodzajZapisuDanychCombo.currentText()	
		res = self.query.exec_("UPDATE Metadane SET Rodzaj_zapisu_danych = '" + value + "' WHERE ID_Metadane = " + str(self.selectedID))
		if res == False:
				QMessageBox.warning(self, "Blad", "Nie mozna wykonac polecenia SQL dla obecnej bazy danych!", QMessageBox.Ok, QMessageBox.Ok)

	def clearMetadata(self):
		self.disabledCellChanged = True
		for i in range(0, 15):
				self.ui.metadataTable.setItem(i, 1, QTableWidgetItem())
		self.disabledCellChanged = False
	
	def closeEvent(self, event):
		result = QMessageBox.question(self, "Wyjscie", "Czy na pewno chcesz wyjsc?",
		QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		
		if result == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	
	def resizeEvent(self, event):
		#QMainWindow.resizeEvent(event)
		if(self.image.isNull() == False):
			self.ui.pic_lab.setPixmap(QPixmap.fromImage(self.image.scaledToHeight(self.ui.Picture.height()-18)))
		else:
			self.ui.pic_lab.setPixmap(QPixmap())
			
	def getLocalisationFromDB(self):
		self.query = QSqlQuery("SELECT DISTINCT Lokalizacja, Miejsce FROM Metadane ORDER BY Lokalizacja, Miejsce")
		self.ui.listWidget.clear()
		self.lokalizacja = []
		ID = 0
		while self.query.next():
			ID = ID + 1
			lokalizacja = self.query.value(0)
			miejsce = self.query.value(1)
			self.lokalizacja.append([lokalizacja, miejsce, ID])
			if miejsce != '':
				self.ui.listWidget.addItem(lokalizacja + " [" + miejsce + "]")
			else:
				self.ui.listWidget.addItem(lokalizacja)
	
	def about(self):
		dialog = QDialog(self)
		ui = Ui_aboutDialog()
		ui.setupUi(dialog)
		dialog.exec_()
		
def main():
	app = QApplication(sys.argv)
	mainWindow = MainWindow()

	sys.exit(app.exec_())
	
if __name__=="__main__":
	main()

