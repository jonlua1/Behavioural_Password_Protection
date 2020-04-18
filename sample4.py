# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

#Customized button image comes from: https://icons8.com


from PyQt5 import QtCore, QtGui, QtWidgets
from dialogBox import Ui_Dialog;


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        width = QtWidgets.QDesktopWidget().screenGeometry(-1).width()
        height = QtWidgets.QDesktopWidget().screenGeometry(-1).height()
        MainWindow.setObjectName("MainWindow")
        #there shouldn't be a hard coded number here in setGeometry
        MainWindow.setGeometry(0,0,width, height)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, width, height))
        self.label.setProperty("class", "backgroundImage")
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("images/background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(round((MainWindow.width() - 900) / 2), 0, 900, 150))
        self.textBrowser.setObjectName("textBrowser")

        self.label_selectBrowser = QtWidgets.QLabel(self.centralwidget)
        self.label_selectBrowser.setGeometry(QtCore.QRect(round((MainWindow.width() - (width / 5) ) / 2), self.textBrowser.y() + self.textBrowser.height() + 50, round(width/5), 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_selectBrowser.setFont(font)
        self.label_selectBrowser.setAutoFillBackground(True)
        self.label_selectBrowser.setObjectName("label_selectBrowser")
        self.label_selectBrowser.setProperty("class", "displayText_selectBrowser")
       
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(round((MainWindow.width() - 1200) / 2), self.label_selectBrowser.y() + 100, 1200, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_checkBox = QtWidgets.QWidget(self.centralwidget)
        self.layout_checkBox.setGeometry(QtCore.QRect(round((MainWindow.width() - 1200) / 2), height - round(height / 6 * 4) + 100, 1200, 100))
        self.layout_checkBox.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.layout_checkBox.setObjectName("layoutWidget_vertical")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layout_checkBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_checkBox = QtWidgets.QHBoxLayout()
        self.horizontalLayout_checkBox.setObjectName("horizontalLayout_checkBox")
        
        self.horizontalLayout_comboBox = QtWidgets.QHBoxLayout()
        self.horizontalLayout_comboBox.setContentsMargins(0,0,0,0)
        self.horizontalLayout_comboBox.setObjectName("horizontalLayout_comboBox")

        self.checkBox_Alphabet = QtWidgets.QCheckBox(self.layout_checkBox)
        self.checkBox_Alphabet.setEnabled(True)
        #self.checkBox_Alphabet.setGeometry(QtCore.QRect(30, 450, 91, 31))
        self.checkBox_Alphabet.setCheckable(True)
        self.checkBox_Alphabet.setObjectName("checkBox_Alphabet")
        self.horizontalLayout_checkBox.addWidget(self.checkBox_Alphabet)
        self.verticalLayout.addLayout(self.horizontalLayout_checkBox)
        self.checkBox_Number = QtWidgets.QCheckBox(self.layout_checkBox)
        self.checkBox_Number.setEnabled(True)
        #self.checkBox_Number.setGeometry(QtCore.QRect(150, 450, 91, 31))
        self.checkBox_Number.setCheckable(True)
        self.checkBox_Number.setObjectName("checkBox_Number")
        self.horizontalLayout_checkBox.addWidget(self.checkBox_Number)
        self.verticalLayout.addLayout(self.horizontalLayout_checkBox)
        self.checkBox_Symbol = QtWidgets.QCheckBox(self.layout_checkBox)
        self.checkBox_Symbol.setEnabled(True)
        #self.checkBox_Symbol.setGeometry(QtCore.QRect(270, 450, 91, 31))
        self.checkBox_Symbol.setCheckable(True)
        self.checkBox_Symbol.setObjectName("checkBox_Symbol")
        self.horizontalLayout_checkBox.addWidget(self.checkBox_Symbol)
        self.verticalLayout.addLayout(self.horizontalLayout_checkBox)

        self.comboBox_Alphabet = QtWidgets.QComboBox(self.layout_checkBox)
        self.comboBox_Alphabet.setEnabled(False)
        #self.comboBox_Alphabet.setGeometry(QtCore.QRect(30, 500, 81, 41))
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
        self.horizontalLayout_comboBox.addWidget(self.comboBox_Alphabet)
        self.verticalLayout.addLayout(self.horizontalLayout_comboBox)
        self.comboBox_Number = QtWidgets.QComboBox(self.layout_checkBox)
        self.comboBox_Number.setEnabled(False)
        #self.comboBox_Number.setGeometry(QtCore.QRect(150, 500, 81, 41))
        self.comboBox_Number.setObjectName("comboBox_Number")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.comboBox_Number.addItem("")
        self.horizontalLayout_comboBox.addWidget(self.comboBox_Number)
        self.comboBox_Symbol = QtWidgets.QComboBox(self.layout_checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_comboBox)
        self.comboBox_Symbol.setEnabled(False)
        #self.comboBox_Symbol.setGeometry(QtCore.QRect(270, 500, 81, 41))
        self.comboBox_Symbol.setObjectName("comboBox_Symbol")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.comboBox_Symbol.addItem("")
        self.horizontalLayout_comboBox.addWidget(self.comboBox_Symbol)
        self.verticalLayout.addLayout(self.horizontalLayout_comboBox)
        self.comboBox_Number_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Number_2.setEnabled(True)
        self.comboBox_Number_2.setGeometry(QtCore.QRect(round((MainWindow.width( ) - 81) / 2), height - round(height / 6 * 2), 81, 41))
        self.comboBox_Number_2.setObjectName("comboBox_Number_2")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")


        self.genPwd = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons8-privacy-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genPwd.setIcon(icon5)
        self.genPwd.setIconSize(QtCore.QSize(80,80))
        self.genPwd.setEnabled(True)
        self.genPwd.setGeometry(QtCore.QRect(round((MainWindow.width() - 450) / 2), height - round(height / 6), 450, 125))
        self.genPwd.setAutoFillBackground(False)
        self.genPwd.setStyleSheet("")
        self.genPwd.setCheckable(False)
        self.genPwd.setChecked(False)
        self.genPwd.setFlat(False)
        self.genPwd.setObjectName("genPwd")
        self.genPwd.setProperty("class", "genPwdBtn")
        self.chromeButton = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton.setIcon(icon1)
        self.chromeButton.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton.setObjectName("chromeButton")
        self.chromeButton.setFixedHeight(80)
        self.chromeButton.setFixedWidth(250)
        self.chromeButton.setProperty("class", "browserBtns")
        self.horizontalLayout.addWidget(self.chromeButton)
        self.FireFoxButton = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton.setIcon(icon2)
        self.FireFoxButton.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton.setObjectName("FireFoxButton")
        self.FireFoxButton.setFixedHeight(80)
        self.FireFoxButton.setFixedWidth(250)
        self.FireFoxButton.setProperty("class", "browserBtns")
        self.horizontalLayout.addWidget(self.FireFoxButton)
        self.OperaButton = QtWidgets.QPushButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OperaButton.setIcon(icon3)
        self.OperaButton.setIconSize(QtCore.QSize(40, 40))
        self.OperaButton.setObjectName("OperaButton")
        self.OperaButton.setFixedHeight(80)
        self.OperaButton.setFixedWidth(250)
        self.OperaButton.setProperty("class", "browserBtns")
        self.horizontalLayout.addWidget(self.OperaButton)
        self.MicrosoftEdgeButton = QtWidgets.QPushButton(self.layoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons8-microsoft-edge-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrosoftEdgeButton.setIcon(icon4)
        self.MicrosoftEdgeButton.setIconSize(QtCore.QSize(40, 40))
        self.MicrosoftEdgeButton.setObjectName("MicrosoftEdgeButton")
        self.MicrosoftEdgeButton.setFixedHeight(80)
        self.MicrosoftEdgeButton.setFixedWidth(250)
        self.MicrosoftEdgeButton.setProperty("class", "browserBtns")
        self.horizontalLayout.addWidget(self.MicrosoftEdgeButton)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon5)
        self.exitButton.setIconSize(QtCore.QSize(80, 80))
        self.exitButton.setGeometry(QtCore.QRect(width - 255, 0, 250, 100))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setProperty("class", "exitBtn")
        MainWindow.setCentralWidget(self.centralwidget)
       
        self.label_noOfWords = QtWidgets.QLabel(self.centralwidget)
        self.label_noOfWords.setGeometry(QtCore.QRect(round((MainWindow.width() - 340) / 2), height - round(height / 6 * 2.5), 340, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_noOfWords.setFont(font)
        self.label_noOfWords.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_noOfWords.setObjectName("label_noOfWords")
    
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.MicrosoftEdgeButton.clicked.connect(self.getButtonName)
        self.OperaButton.clicked.connect(self.getButtonName)
        self.chromeButton.clicked.connect(self.getButtonName)
        self.FireFoxButton.clicked.connect(self.getButtonName)
        self.genPwd.clicked.connect(self.getPWD)
        self.exitButton.clicked.connect(self.exitSystem)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

###############################Function re-work is needed###########################################################################

        self.checkBox_Alphabet.stateChanged.connect(self.toggleComboBox_Alphabet)
        self.checkBox_Number.stateChanged.connect(self.toggleComboBox_Number)
        self.checkBox_Symbol.stateChanged.connect(self.toggleComboBox_Symbol)

    def toggleComboBox_Alphabet(self, state):
        if state > 0:
            self.comboBox_Alphabet.setEnabled(True)
        else:
            self.comboBox_Alphabet.setEnabled(False)

    def toggleComboBox_Number(self, state):
        if state > 0:
            self.comboBox_Number.setEnabled(True)
        else:
            self.comboBox_Number.setEnabled(False)

    def toggleComboBox_Symbol(self, state):
        if state > 0:
            self.comboBox_Symbol.setEnabled(True)
        else:
            self.comboBox_Symbol.setEnabled(False)

    def getButtonName(self):
        name = MainWindow.sender()
        print('%s Clicked!' % str(name.objectName()))
        
        if name.objectName() == 'chromeButton':
            self.label_selectBrowser.setText("Chrome is selected!")
            self.updateLabelSize()

        elif name.objectName() == 'OperaButton':
            self.label_selectBrowser.setText("Opera is selected!")
            self.updateLabelSize()

        elif name.objectName() == 'MicrosoftEdgeButton':
            self.label_selectBrowser.setText("Microsoft Edge is selected!")
            self.updateLabelSize()

        elif name.objectName() == 'FireFoxButton':
            self.label_selectBrowser.setText("FireFox is selected!")
            self.updateLabelSize()


##################################################################################################################################            

    def exitSystem(self, event):

        reply = QtWidgets.QMessageBox.question(
            MainWindow, "Message" , "Are you sure you want to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            app.quit()

        else: 
            pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


    def updateLabelSize(self):
        self.label_selectBrowser.adjustSize()

    def getPWD(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

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
        self.genPwd.setText(_translate("MainWindow", "Generate Password"))
        self.comboBox_Number.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_Number.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_Number.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_Number.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_Number.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_Number.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_Number.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_Number.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_Number.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_Number.setItemText(9, _translate("MainWindow", "0"))
        self.checkBox_Number.setText(_translate("MainWindow", "Number"))
        self.checkBox_Symbol.setText(_translate("MainWindow", "Symbol"))
        self.comboBox_Symbol.setItemText(0, _translate("MainWindow", "!"))
        self.comboBox_Symbol.setItemText(1, _translate("MainWindow", "@"))
        self.comboBox_Symbol.setItemText(2, _translate("MainWindow", "#"))
        self.comboBox_Symbol.setItemText(3, _translate("MainWindow", "$"))
        self.comboBox_Symbol.setItemText(4, _translate("MainWindow", "%"))
        self.comboBox_Symbol.setItemText(5, _translate("MainWindow", "^"))
        self.comboBox_Symbol.setItemText(6, _translate("MainWindow", "&"))
        self.comboBox_Symbol.setItemText(7, _translate("MainWindow", "*"))
        self.comboBox_Symbol.setItemText(8, _translate("MainWindow", "?"))
        self.label_selectBrowser.setText(_translate("MainWindow", "Select Your Browser"))
        self.chromeButton.setText(_translate("MainWindow", "Google Chrome"))
        self.FireFoxButton.setText(_translate("MainWindow", "FireFox"))
        self.OperaButton.setText(_translate("MainWindow", "Opera"))
        self.MicrosoftEdgeButton.setText(_translate("MainWindow", "Microsoft Edge"))
        self.label_noOfWords.setText(_translate("MainWindow", "Select number of words"))
        self.comboBox_Number_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_Number_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_Number_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_Number_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_Number_2.setItemText(4, _translate("MainWindow", "5"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.styleSheet = """

        QMainWindow {
            background-color: #ede0bb;
        }

        .backgroundImage{
            border-style: outset;
        }

        QLabel {
            text-align: center;
            background-color: #ffffff;
        }

        .browserBtns{
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color:#7892c2;
            border-radius:30px;
            border:2px solid #4e6096;
            color:#ffffff;
            font-family:Trebuchet MS;
            font-size:19px;
            font-weight:bold;
        
            text-decoration:none;
        }

        .displayText_selectBrowser {
            text-align: right;
        }
        
        QCheckBox::indicator {
            width: 100px;
            height: 100px;
        }

        QCheckBox::indicator:unchecked{
            image: url(images/icons8-unchecked-checkbox-100.png)
        }

        QCheckBox::indicator:checked{
            image: url(images/icons8-checkmark-100.png)
        }

        .genPwdBtn {
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color:#7892c2;
            border-radius:30px;
            border:2px solid #4e6096;
            color:#ffffff;
            font-family:Trebuchet MS;
            font-size:19px;
            font-weight:bold;
            padding:25px 59px;
            text-decoration:none;
          
        }
        .genPwdBtn:hover {
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        .genPwdBtn:active {
            position:relative;
            top:1px;
        }



    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
