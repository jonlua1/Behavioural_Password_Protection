# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

#Icon of Buttons come from : https://icons8.com !!! 


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(round((MainWindow.width() - 1300) / 2), round((MainWindow.height() - 450 ) / 7 *6), 1300, 450))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.container_1 = QtWidgets.QWidget()
        self.container_1.setProperty("class", "containers")
        self.gridLayout = QtWidgets.QGridLayout(self.container_1)
        self.gridLayout.setContentsMargins(25, 10, 15, 10)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setProperty("class", "label_Title")
        self.label_Title.setGeometry(QtCore.QRect(self.groupBox.x() + 20, self.groupBox.y() - 70, 300, 70))

        #buttons
        self.chromeButton = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton.setIcon(icon1)
        self.chromeButton.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton.setObjectName("chromeButton")
        self.FireFoxButton = QtWidgets.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton.setIcon(icon2)
        self.FireFoxButton.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton.setObjectName("FireFoxButton")
        self.MicrosoftEdge = QtWidgets.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons8-microsoft-edge-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrosoftEdge.setIcon(icon3)
        self.MicrosoftEdge.setIconSize(QtCore.QSize(40, 40))
        self.MicrosoftEdge.setObjectName("MicrosoftEdge")
        self.OperaButton = QtWidgets.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OperaButton.setIcon(icon4)
        self.OperaButton.setIconSize(QtCore.QSize(40, 40))
        self.OperaButton.setObjectName("OperaButton")
        
        self.label_selectBrowser = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectBrowser.setFont(font)
        self.label_selectBrowser.setAutoFillBackground(False)
        self.label_selectBrowser.setObjectName("label_selectBrowser")

        self.gridLayout.addWidget(self.chromeButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.FireFoxButton, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.MicrosoftEdge, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.OperaButton, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.label_selectBrowser, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.container_1)

        self.container_2 = QtWidgets.QWidget()
        self.container_2.setProperty("class", "containers")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.container_2)
        self.gridLayout_2.setContentsMargins(25, 10, 15, 10)
        self.gridLayout_2.setHorizontalSpacing(16)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.genPwd = QtWidgets.QPushButton(self.groupBox)
        self.genPwd.setEnabled(True)
        self.genPwd.setAutoFillBackground(False)
        self.genPwd.setProperty("class", "btn")
        self.genPwd.setCheckable(False)
        self.genPwd.setChecked(False)
        self.genPwd.setFlat(False)
        self.genPwd.setObjectName("genPwd")
        
        self.comboBox_Number_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Number_2.setEnabled(True)
        self.comboBox_Number_2.setObjectName("comboBox_Number_2")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        self.comboBox_Number_2.addItem("")
        
        self.comboBox_Number_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Number_3.setEnabled(True)
        self.comboBox_Number_3.setObjectName("comboBox_Number_3")
        self.comboBox_Number_3.addItem("")
        
        self.dummyLabel_1 = QtWidgets.QLabel(self.groupBox)
        self.dummyLabel_1.setObjectName("dummyLabel_1")
        
        self.label_selectPreference = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectPreference.setFont(font)
        self.label_selectPreference.setAutoFillBackground(True)
        self.label_selectPreference.setObjectName("label_selectPreference")
        
        self.dummyLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.dummyLabel_2.setObjectName("dummyLabel_2")

        self.gridLayout_2.addWidget(self.label_selectPreference, 0, 0, 1, 4)
        self.gridLayout_2.addWidget(self.comboBox_Number_2, 1, 1, 1, 3)
        self.gridLayout_2.addWidget(self.comboBox_Number_3, 2, 1, 1, 3)
        self.gridLayout_2.addWidget(self.dummyLabel_1, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.dummyLabel_2, 1, 4, 1, 1)
        self.gridLayout_2.addWidget(self.genPwd, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.container_2)

        self.logoBackground = QtWidgets.QLabel(self.centralwidget)
        self.logoBackground.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 250))
        self.logoBackground.setProperty("class", "logoBackground")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect( round((MainWindow.width() - 560) / 2 ), 30, 560, 150))
        self.label.setPixmap(QtGui.QPixmap("./images/ezPassLogo.PNG"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setProperty("class", "label_logo")

        self.layoutWidget_1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_1.setGeometry(QtCore.QRect(0, self.logoBackground.height() - 30, MainWindow.width(), 100)) 
        self.layoutWidget_1.setProperty("class", "navBar")

        self.HomeBtn = QtWidgets.QPushButton(self.layoutWidget_1)
        self.HomeBtn.setProperty("class", "navBar_btn")
        self.VaultBtn = QtWidgets.QPushButton(self.layoutWidget_1)
        self.VaultBtn.setProperty("class", "navBar_btn")
        self.SettingsBtn = QtWidgets.QPushButton(self.layoutWidget_1)
        self.SettingsBtn.setProperty("class", "navBar_btn")
        self.AboutUsBtn = QtWidgets.QPushButton(self.layoutWidget_1)
        self.AboutUsBtn.setProperty("class", "navBar_btn")
        self.dummyLabel_3 = QtWidgets.QLabel(self.layoutWidget_1)
        self.dummyLabel_4 = QtWidgets.QLabel(self.layoutWidget_1)

        self.navBar = QtWidgets.QHBoxLayout(self.layoutWidget_1)
        self.navBar.addWidget(self.HomeBtn)
        self.navBar.addWidget(self.VaultBtn)
        self.navBar.addWidget(self.SettingsBtn)
        self.navBar.addWidget(self.AboutUsBtn)
        self.navBar.addWidget(self.dummyLabel_3)
        self.navBar.addWidget(self.dummyLabel_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2000, 18))
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
        self.chromeButton.setText(_translate("MainWindow", "Google Chrome"))
        self.FireFoxButton.setText(_translate("MainWindow", "FireFox"))
        self.MicrosoftEdge.setText(_translate("MainWindow", "Microsoft Edge"))
        self.OperaButton.setText(_translate("MainWindow", "Opera"))
        self.HomeBtn.setText(_translate("MainWindow", "Home"))
        self.VaultBtn.setText(_translate("MainWindow", "Vault"))
        self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn.setText(_translate("MainWindow", "About Us"))
        self.label_selectBrowser.setText(_translate("MainWindow", "1. Select browser"))
        self.genPwd.setText(_translate("MainWindow", "Generate Password"))
        self.comboBox_Number_2.setItemText(0, _translate("MainWindow", "Number of words"))
        self.comboBox_Number_2.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_Number_2.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_Number_2.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_Number_2.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_Number_2.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_Number_3.setItemText(0, _translate("MainWindow", "Preference(s)"))
        self.dummyLabel_1.setText(_translate("MainWindow", ""))
        self.label_selectPreference.setText(_translate("MainWindow", "2. Select number of words & Preferences"))
        self.dummyLabel_2.setText(_translate("MainWindow", ""))
        self.dummyLabel_3.setText(_translate("MainWindow", ""))
        self.dummyLabel_4.setText(_translate("MainWindow", ""))
        self.label_Title.setText(_translate("MainWindow", "Generate Passphrase"))
        self.label.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.styleSheet = """
         QPushButton {
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color:#34363a;
            border-radius:39px;
            border:2px solid #34363a;
            color:#d2c15d;
            font-family:Trebuchet MS;
            font-size:19px;
            font-weight:bold;
            padding:20px 54px;
            text-decoration:none;
          
        }
        QPushButton:hover {
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        QPushButton:active {
            position:relative;
            top:1px;
        }

        .btn {
            border-radius: 30px;
        }

        QGroupBox {
            background-color:#34363a;
            border: none;
        }

        QLabel {
            color:#34363a; 
            background-color:#d2c15d;
        }

        .containers {
            background-color: #d2c15d;
            padding-bottom: 20px;
            border-radius:50px;
            border:2px solid #34363a;
        }

        QComboBox{
            background-color:#34363a;
            color:#d2c15d;
            font-size: 20px;
            padding-top: 5px;
            padding-bottom: 5px;
            padding-left: 10px;
        }

        QComboBox::down-arrow{
            image: url(./images/icons8-sort-down-100.png);
        }

        QMainWindow{
            background-color: #34363a;
        }

        .label_Title {
            font-size: 30px;
            color: #d2c15d;
            background-color:#34363a;
        }

        .label_logo {
            border: none;
        }

        .logoBackground {
            background-color: #454547;
         }

        .navBar_btn {
            color: #34363a;
            background-color: #d2c15d;
            border: none;
            text-align: left;
            font-size: 30px;
        }

        .navBar {
            background-color: #d2c15d;
        }
    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
