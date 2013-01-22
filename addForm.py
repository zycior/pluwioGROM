# -*- coding: utf-8 -*-

import sys
import hashlib
import shutil
import os.path
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from addFormUI import Ui_addDialog

def md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data.encode('latin-1'))
    return md5.hexdigest()

class addDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		
		#interface z QtDesignera
		self.ui = Ui_addDialog()
		self.ui.setupUi(self)
		
		self.ID_to_delete = []
		self.pluwiogramy = []
		self.ID_Metadane = -1
		
		self.ui.btnOK.clicked.connect(self.insertValuesToDB)
		self.connect(self.ui.lokalizacja, SIGNAL("textChanged(const QString&)"), self.btnBlockade)
		self.connect(self.ui.pathEdit, SIGNAL("textChanged(const QString&)"), self.pathChanged)
		self.ui.btnAdd.clicked.connect(self.addEntryStart)
		self.ui.btnDel.clicked.connect(self.delEntry)
		self.ui.applyMetadata.clicked.connect(self.metadataApplied)
		self.ui.btnBrowse.clicked.connect(self.browse)
		self.ui.btnApply.clicked.connect(self.addEntry)
		self.ui.listWidget.itemSelectionChanged.connect(self.selChanged)
	
	def prepareToShow(self, values):
		self.clearEntries()
		self.setValues(values)
		self.ui.groupBox.setEnabled(True)
		self.ui.groupBox_2.setEnabled(False)
		self.ui.btnOK.setEnabled(False)
		self.btnBlockade("")
		self.ID_to_delete = []
	
	def setValues(self, values):
		self.ui.mierzonyParametr.setText(values[0])
		self.ui.przyrzadPomiarowy.setText(values[1])
		self.ui.metodaPomiaru.setCurrentIndex(values[2])
		self.ui.rodzajZapisuDanych.setCurrentIndex(values[3])
		self.ui.cechyWykresu.setText(values[4])
		self.ui.jednostkaPomiarowa.setText(values[5])
		self.ui.dokladnoscPomiarowa.setText(values[6])
		self.ui.skalaPomiaru.setText(values[7])
		self.ui.lokalizacja.setText(values[8])
		self.ui.miejsce.setText(values[9])
		self.ui.obserwator.setText(values[10])
		self.ui.czestotliwoscPomiaru.setText(values[11])
		self.ui.stacjaPomiarowa.setCurrentIndex(values[12])
		self.ui.uwagi.setText(values[13])
		
	def clearEntries(self):
		self.ui.listWidget.clear()
		self.ui.pathEdit.setText("")
		self.ui.dateEdit.setDate(QDate.currentDate())
		self.ui.nowyPomiar.setEnabled(False)
		self.ui.btnAdd.setEnabled(True)
		self.ui.btnDel.setEnabled(False)
		self.pluwiogramy = []
	
	def metadataApplied(self):
		v = []
		v.append(self.ui.mierzonyParametr.text())
		v.append(self.ui.przyrzadPomiarowy.text())
		v.append(self.ui.metodaPomiaru.currentText())
		v.append(self.ui.rodzajZapisuDanych.currentText())
		v.append(self.ui.cechyWykresu.text())
		v.append(self.ui.jednostkaPomiarowa.text())
		v.append(self.ui.dokladnoscPomiarowa.text())
		v.append(self.ui.skalaPomiaru.text())
		v.append(self.ui.lokalizacja.text())
		v.append(self.ui.miejsce.text())
		v.append(self.ui.obserwator.text())
		v.append(self.ui.czestotliwoscPomiaru.text())
		v.append(self.ui.stacjaPomiarowa.currentText())
		v.append(self.ui.uwagi.toPlainText())
		sql = "SELECT ID_Metadane FROM Metadane WHERE Mierzony_parametr='"+v[0]+"' AND Przyrzad_pomiarowy='" + v[1]+"' AND "\
		"Metoda_pomiaru='"+v[2]+"' AND Rodzaj_zapisu_danych='"+v[3]+"' AND Cechy_wykresu_danych='"+v[4]+"' AND Jednostka_pomiarowa='"+v[5]+"' AND "\
		"Dokladnosc_pomiarowa='"+v[6]+"' AND Skala_pomiaru='"+v[7]+"' AND lokalizacja='"+v[8]+"' AND miejsce='"+v[9]+"' AND obserwator='"+v[10]+"' AND "\
		"Czestotliwosc_pomiaru='"+v[11]+"' AND Stacja_pomiarowa='"+v[12]+"' AND uwagi='"+v[13]+"'"
		query = QSqlQuery(sql)
		
		if query.next():
			self.ID_Metadane = query.value(0)
			query = QSqlQuery("SELECT ID, Data, Sciezka FROM Pluwiogram WHERE ID_Metadane = " + str(self.ID_Metadane) + " ORDER BY Data")
			while query.next():
				self.pluwiogramy.append([query.value(1), query.value(2), query.value(0)])
				self.ui.listWidget.addItem(query.value(1))
			self.formBlockade()
		else:
			self.ID_Metadane = -1
		
		self.ui.groupBox_2.setEnabled(True)
		self.ui.groupBox.setEnabled(False)
	def insertValuesToDB(self):
		
		if self.ID_Metadane == -1:
			v = []
			v.append(self.ui.mierzonyParametr.text())
			v.append(self.ui.przyrzadPomiarowy.text())
			v.append(self.ui.metodaPomiaru.currentText())
			v.append(self.ui.rodzajZapisuDanych.currentText())
			v.append(self.ui.cechyWykresu.text())
			v.append(self.ui.jednostkaPomiarowa.text())
			v.append(self.ui.dokladnoscPomiarowa.text())
			v.append(self.ui.skalaPomiaru.text())
			v.append(self.ui.lokalizacja.text())
			v.append(self.ui.miejsce.text())
			v.append(self.ui.obserwator.text())
			v.append(self.ui.czestotliwoscPomiaru.text())
			v.append(self.ui.stacjaPomiarowa.currentText())
			v.append(self.ui.uwagi.toPlainText())
			sql = "INSERT INTO Metadane VALUES (NULL"
			for i in v:
				sql = sql + ", '"+ i + "'"
			sql = sql+")"
			query = QSqlQuery()
			if query.exec_(sql):
				query = QSqlQuery("SELECT max(ID_Metadane) FROM Metadane")
				if query.next():
					self.ID_Metadane = query.value(0)
				else:
					QMessageBox.warning(self, "Blad", "Niepowodzenie przy wykonaniu zapytania do bazy danych", QMessageBox.Ok, QMessageBox.Ok)
					self.reject()
			else:
				QMessageBox.warning(self, "Blad", "Niepowodzenie przy tworzeniu nowego wpisu: " + query.lastError().text(), QMessageBox.Ok, QMessageBox.Ok)
				self.reject()
		for i in self.pluwiogramy:
			if i[2] == -1:
				filename, extension = os.path.splitext(i[1])
				file = open(i[1], encoding='latin-1')
				hash = md5_for_file(file)
				if os.path.isfile(".\\data\\" + hash) == False:
					shutil.copyfile(i[1], ".\\data\\"+ hash + extension)
				sql = "INSERT INTO Pluwiogram VALUES(NULL, " + str(self.ID_Metadane) +", '" + i[0] + "', '.\\data\\" + hash + extension + "')"
				query = QSqlQuery()
				query_result = query.exec_(sql)
				if query_result == False:
					QMessageBox.warning(self, "Blad", "Niepowodzenie przy tworzeniu nowego wpisu: " + query.lastError().text(), QMessageBox.Ok, QMessageBox.Ok)
					break
		
		for i in self.ID_to_delete:
			query.exec_("DELETE FROM Pluwiogram WHERE ID = " + str(i[0]))
			query = QSqlQuery("SELECT count(ID) FROM Pluwiogram WHERE Sciezka='" + i[1] +"'")
			if query.next() and int(query.value(0)) == 0:
					try:
						os.remove(i[1])
					except OSError:
						QMessageBox.critical(self, "Blad", "Proba usuniecia pliku pluwiogramu zakonczyla sie niepowodzeniem!", QMessageBox.Ok, QMessageBox.Ok)
		self.accept()

	def addEntryStart(self):
		self.ui.pathEdit.setText("")
		self.ui.nowyPomiar.setEnabled(True)
		self.ui.dateEdit.setDate(QDate.currentDate())
	
	def addEntry(self):
		date = self.ui.dateEdit.date().toString(Qt.ISODate)
		self.pluwiogramy.append([date, self.ui.pathEdit.text(), -1])
		self.ui.listWidget.addItem(date)
		self.ui.pathEdit.setText("")
		self.ui.nowyPomiar.setEnabled(False)
		self.formBlockade()
		
	def delEntry(self):
		index = self.ui.listWidget.currentRow()
		self.ui.listWidget.takeItem(index)
		if self.pluwiogramy[index][2] != -1:
			self.ID_to_delete.append([self.pluwiogramy[index][2], self.pluwiogramy[index][1]])
		del self.pluwiogramy[index]
		self.ui.formBlockade()
		
	def browse(self):
		path = QFileDialog.getOpenFileName(self,"Otworz plik", ".","Pliki graficzne(*.jpg *.jpeg *.bmp *.png)")	
		if path == "":
			return
		self.ui.pathEdit.setText(path)
	
	def pathChanged(self, text):
		self.ui.btnApply.setEnabled(text != "")
	
	def btnBlockade(self, text):
		self.ui.applyMetadata.setEnabled(self.ui.lokalizacja.text() != "")
	
	def formBlockade(self):
		self.ui.btnOK.setEnabled(len(self.pluwiogramy) > 0 and self.ui.lokalizacja.text() != "")
	
	def selChanged(self):
		self.ui.btnDel.setEnabled(self.ui.listWidget.currentRow() != -1)