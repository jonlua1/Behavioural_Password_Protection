# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/whitecat.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.checkBox_Alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Alphabet.setEnabled(True)
        self.checkBox_Alphabet.setGeometry(QtCore.QRect(30, 450, 81, 31))
        self.checkBox_Alphabet.setCheckable(True)
        self.checkBox_Alphabet.setObjectName("checkBox_Alphabet")
        self.comboBox_Alphabet = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Alphabet.setEnabled(False)
        self.comboBox_Alphabet.setGeometry(QtCore.QRect(30, 500, 81, 41))
        self.comboBox_Alphabet.setObjectName("comboBox_Alphabet")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.comboBox_Alphabet.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 40, 481, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.fileLocation = QtWidgets.QPushButton(self.centralwidget)
        self.fileLocation.setGeometry(QtCore.QRect(10, 210, 251, 41))
        self.fileLocation.setObjectName("fileLocation")
        self.genPwd = QtWidgets.QPushButton(self.centralwidget)
        self.genPwd.setEnabled(False)
        self.genPwd.setGeometry(QtCore.QRect(390, 500, 191, 41))
        self.genPwd.setAutoFillBackground(False)
        self.genPwd.setStyleSheet("\n"
"")
        self.genPwd.setCheckable(False)
        self.genPwd.setChecked(False)
        self.genPwd.setFlat(False)
        self.genPwd.setObjectName("genPwd")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(150, 500, 81, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox_Alphabet_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Alphabet_2.setEnabled(True)
        self.checkBox_Alphabet_2.setGeometry(QtCore.QRect(150, 450, 81, 31))
        self.checkBox_Alphabet_2.setCheckable(True)
        self.checkBox_Alphabet_2.setObjectName("checkBox_Alphabet_2")
        self.checkBox_Alphabet_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Alphabet_3.setEnabled(True)
        self.checkBox_Alphabet_3.setGeometry(QtCore.QRect(270, 450, 81, 31))
        self.checkBox_Alphabet_3.setCheckable(True)
        self.checkBox_Alphabet_3.setObjectName("checkBox_Alphabet_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 500, 81, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EzPass"))
        self.checkBox_Alphabet.setText(_translate("MainWindow", "Alphabet"))
        self.comboBox_Alphabet.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_Alphabet.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_Alphabet.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox_Alphabet.setItemText(3, _translate("MainWindow", "D"))
        self.comboBox_Alphabet.setItemText(4, _translate("MainWindow", "E"))
        self.comboBox_Alphabet.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox_Alphabet.setItemText(6, _translate("MainWindow", "G"))
        self.comboBox_Alphabet.setItemText(7, _translate("MainWindow", "H"))
        self.comboBox_Alphabet.setItemText(8, _translate("MainWindow", "I"))
        self.comboBox_Alphabet.setItemText(9, _translate("MainWindow", "J"))
        self.comboBox_Alphabet.setItemText(10, _translate("MainWindow", "K"))
        self.comboBox_Alphabet.setItemText(11, _translate("MainWindow", "L"))
        self.comboBox_Alphabet.setItemText(12, _translate("MainWindow", "M"))
        self.comboBox_Alphabet.setItemText(13, _translate("MainWindow", "N"))
        self.comboBox_Alphabet.setItemText(14, _translate("MainWindow", "O"))
        self.comboBox_Alphabet.setItemText(15, _translate("MainWindow", "P"))
        self.comboBox_Alphabet.setItemText(16, _translate("MainWindow", "Q"))
        self.comboBox_Alphabet.setItemText(17, _translate("MainWindow", "R"))
        self.comboBox_Alphabet.setItemText(18, _translate("MainWindow", "S"))
        self.comboBox_Alphabet.setItemText(19, _translate("MainWindow", "T"))
        self.comboBox_Alphabet.setItemText(20, _translate("MainWindow", "U"))
        self.comboBox_Alphabet.setItemText(21, _translate("MainWindow", "V"))
        self.comboBox_Alphabet.setItemText(22, _translate("MainWindow", "W"))
        self.comboBox_Alphabet.setItemText(23, _translate("MainWindow", "X"))
        self.comboBox_Alphabet.setItemText(24, _translate("MainWindow", "Y"))
        self.comboBox_Alphabet.setItemText(25, _translate("MainWindow", "Z"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Guide: How to generate a password</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt;\"><br /></p></body></html>"))
        self.fileLocation.setText(_translate("MainWindow", "Choose Browser"))
        self.genPwd.setText(_translate("MainWindow", "Generate Password"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "0"))
        self.checkBox_Alphabet_2.setText(_translate("MainWindow", "Number"))
        self.checkBox_Alphabet_3.setText(_translate("MainWindow", "Symbol"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "!"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "@"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "#"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "$"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "%"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "^"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "&"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "*"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
