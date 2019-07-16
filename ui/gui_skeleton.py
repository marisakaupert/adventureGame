import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "adventureGame.ui"

uiMainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class AdventureGame(QtWidgets.QDialog, uiMainWindow):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		uiMainWindow.__init__(self)
		self.setupUi(self)
		
		

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = AdventureGame()
	window.show()
	sys.exit(app.exec_())




		







