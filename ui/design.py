# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adventureGame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(748, 581)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gameGraphicsView = QtWidgets.QGraphicsView(Dialog)
        self.gameGraphicsView.setObjectName("gameGraphicsView")
        self.verticalLayout.addWidget(self.gameGraphicsView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gameLabel = QtWidgets.QLabel(Dialog)
        self.gameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.gameLabel.setObjectName("gameLabel")
        self.verticalLayout_3.addWidget(self.gameLabel)
        self.descriptionTextEdit = QtWidgets.QTextEdit(Dialog)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.verticalLayout_3.addWidget(self.descriptionTextEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userChoiceLineEdit = QtWidgets.QLineEdit(Dialog)
        self.userChoiceLineEdit.setObjectName("userChoiceLineEdit")
        self.horizontalLayout_3.addWidget(self.userChoiceLineEdit)
        self.enterPushButton = QtWidgets.QPushButton(Dialog)
        self.enterPushButton.setObjectName("enterPushButton")
        self.horizontalLayout_3.addWidget(self.enterPushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.playerProgressBar = QtWidgets.QProgressBar(Dialog)
        self.playerProgressBar.setProperty("value", 0)
        self.playerProgressBar.setObjectName("playerProgressBar")
        self.verticalLayout_3.addWidget(self.playerProgressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gameLabel.setText(_translate("Dialog", "Adventure Game"))
        self.enterPushButton.setText(_translate("Dialog", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

