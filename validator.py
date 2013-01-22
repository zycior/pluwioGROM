# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class metodaPomiaruCombo(QItemDelegate):
	def __init__(self, parent=None):
		QItemDelegate.__init__(self, parent)
		
	def createEditor(self, parent, option, index):
		combo = QComboBox(parent)
		combo.addItem("Automat")
		combo.addItem("Tradycyjna")
		return combo
		
class rodzajZapisuDanychCombo(QItemDelegate):
	def __init__(self, parent=None):
		QItemDelegate.__init__(self, parent)
		
	def createEditor(self, parent, option, index):
		combo = QComboBox(parent)
		combo.addItem("Dziennik")
		combo.addItem("Samopis analogowy")
		combo.addItem("Samopis cyfrowy")
		return combo
		
class stacjaPomiarowaCombo(QItemDelegate):
	def __init__(self, parent=None):
		QItemDelegate.__init__(self, parent)
		
	def createEditor(self, parent, option, index):
		combo = QComboBox(parent)
		combo.addItem("Czynna")
		combo.addItem("Nieczynna")
		return combo
		
