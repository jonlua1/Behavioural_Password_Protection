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
        icon.addPixmap(QtGui.QPixmap("./images/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.page_genPas = QtWidgets.QWidget()
        self.page_genPas.setObjectName("page")
        self.groupBox_genPas = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_genPas.setGeometry(QtCore.QRect(round((MainWindow.width() - 1300) / 2), round((MainWindow.height() - 450 ) / 7 *6), 1300, 450))
        self.groupBox_genPas.setObjectName("groupBox_genPas")
        self.groupBox_genPas.setProperty("class", "QGroupBox_genPas")
        self.verticalLayout_genPas = QtWidgets.QVBoxLayout(self.groupBox_genPas)
        self.verticalLayout_genPas.setObjectName("verticalLayout_genPas")
        self.container_1_genPas = QtWidgets.QWidget()
        self.container_1_genPas.setProperty("class", "containers_genPas")
        self.gridLayout_genPas = QtWidgets.QGridLayout(self.container_1_genPas)
        self.gridLayout_genPas.setContentsMargins(25, 10, 15, 10)
        self.gridLayout_genPas.setHorizontalSpacing(30)
        self.gridLayout_genPas.setVerticalSpacing(10)
        self.gridLayout_genPas.setObjectName("gridLayout_genPas")
        self.label_Title_genPas = QtWidgets.QLabel(self.centralwidget)
        self.label_Title_genPas.setProperty("class", "label_Title_genPas")
        self.label_Title_genPas.setGeometry(QtCore.QRect(self.groupBox_genPas.x() + 20, self.groupBox_genPas.y() - 70, 300, 70))

        #buttons
        self.chromeButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        self.chromeButton_genPas.setProperty("class", "QPushButton_genPas")
        icon1_genPas = QtGui.QIcon()
        icon1_genPas.addPixmap(QtGui.QPixmap("../images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton_genPas.setIcon(icon1_genPas)
        self.chromeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton_genPas.setObjectName("chromeButton_genPas")
        self.FireFoxButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        self.FireFoxButton_genPas.setProperty("class", "QPushButton_genPas")
        icon2_genPas = QtGui.QIcon()
        icon2_genPas.addPixmap(QtGui.QPixmap("../images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton_genPas.setIcon(icon2_genPas)
        self.FireFoxButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton_genPas.setObjectName("FireFoxButton_genPas")
        self.MicrosoftEdgeButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        self.MicrosoftEdgeButton_genPas.setProperty("class", "QPushButton_genPas")
        icon3_genPas = QtGui.QIcon()
        icon3_genPas.addPixmap(QtGui.QPixmap("../images/icons8-microsoft-edge-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrosoftEdgeButton_genPas.setIcon(icon3_genPas)
        self.MicrosoftEdgeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.MicrosoftEdgeButton_genPas.setObjectName("MicrosoftEdgeButton_genPas")
        self.OperaButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        self.OperaButton_genPas.setProperty("class", "QPushButton_genPas")
        icon4_genPas = QtGui.QIcon()
        icon4_genPas.addPixmap(QtGui.QPixmap("../images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OperaButton_genPas.setIcon(icon4_genPas)
        self.OperaButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.OperaButton_genPas.setObjectName("OperaButton_genPas")
        
        self.label_selectBrowser = QtWidgets.QLabel(self.groupBox_genPas)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectBrowser.setFont(font)
        self.label_selectBrowser.setAutoFillBackground(False)
        self.label_selectBrowser.setObjectName("label_selectBrowser")
        self.label_selectBrowser.setProperty("class", "QLabel_genPas")

        self.gridLayout_genPas.addWidget(self.chromeButton_genPas, 1, 0, 1, 1)
        self.gridLayout_genPas.addWidget(self.FireFoxButton_genPas, 1, 1, 1, 1)
        self.gridLayout_genPas.addWidget(self.MicrosoftEdgeButton_genPas, 1, 3, 1, 1)
        self.gridLayout_genPas.addWidget(self.OperaButton_genPas, 1, 2, 1, 1)
        self.gridLayout_genPas.addWidget(self.label_selectBrowser, 0, 0, 1, 2)
        self.verticalLayout_genPas.addWidget(self.container_1_genPas)

        self.container_2_genPas = QtWidgets.QWidget()
        self.container_2_genPas.setProperty("class", "containers_genPas")
        self.gridLayout_2_genPas = QtWidgets.QGridLayout(self.container_2_genPas)
        self.gridLayout_2_genPas.setContentsMargins(25, 10, 15, 10)
        self.gridLayout_2_genPas.setHorizontalSpacing(16)
        self.gridLayout_2_genPas.setVerticalSpacing(10)
        self.gridLayout_2_genPas.setObjectName("gridLayout_2_genPas")
        self.genPwd_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        self.genPwd_genPas.setEnabled(True)
        self.genPwd_genPas.setAutoFillBackground(False)
        self.genPwd_genPas.setProperty("class", "QPushButton_genPas")
        self.genPwd_genPas.setCheckable(False)
        self.genPwd_genPas.setChecked(False)
        self.genPwd_genPas.setFlat(False)
        self.genPwd_genPas.setObjectName("genPwd_genPas")
        
        self.comboBox_Number_2_genPas = QtWidgets.QComboBox(self.groupBox_genPas)
        self.comboBox_Number_2_genPas.setEnabled(True)
        self.comboBox_Number_2_genPas.setObjectName("comboBox_Number_2_genPas")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.setProperty("class", "comboBox_genPas")
        
        self.comboBox_Number_3_genPas = QtWidgets.QComboBox(self.groupBox_genPas)
        self.comboBox_Number_3_genPas.setEnabled(True)
        self.comboBox_Number_3_genPas.setObjectName("comboBox_Number_3_genPas")
        self.comboBox_Number_3_genPas.addItem("")
        self.comboBox_Number_3_genPas.setProperty("class", "comboBox_genPas")
        
        self.dummyLabel_1_genPas = QtWidgets.QLabel(self.groupBox_genPas)
        self.dummyLabel_1_genPas.setObjectName("dummyLabel_1_genPas")
        self.dummyLabel_1_genPas.setProperty("class", "QLabel_genPas")
        
        self.label_selectPreference_genPas = QtWidgets.QLabel(self.groupBox_genPas)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectPreference_genPas.setFont(font)
        self.label_selectPreference_genPas.setAutoFillBackground(True)
        self.label_selectPreference_genPas.setObjectName("label_selectPreference_genPas")
        self.label_selectPreference_genPas.setProperty("class", "QLabel_genPas")
        
        self.dummyLabel_2 = QtWidgets.QLabel(self.groupBox_genPas)
        self.dummyLabel_2.setObjectName("dummyLabel_2")
        self.dummyLabel_2.setProperty("class", "QLabel_genPas")

        self.gridLayout_2_genPas.addWidget(self.label_selectPreference_genPas, 0, 0, 1, 4)
        self.gridLayout_2_genPas.addWidget(self.comboBox_Number_2_genPas, 1, 1, 1, 3)
        self.gridLayout_2_genPas.addWidget(self.comboBox_Number_3_genPas, 2, 1, 1, 3)
        self.gridLayout_2_genPas.addWidget(self.dummyLabel_1_genPas, 1, 0, 1, 1)
        self.gridLayout_2_genPas.addWidget(self.dummyLabel_2, 1, 4, 1, 1)
        self.gridLayout_2_genPas.addWidget(self.genPwd_genPas, 3, 2, 1, 1)
        self.verticalLayout_genPas.addWidget(self.container_2_genPas)

        self.logoBackground_genPas = QtWidgets.QLabel(self.centralwidget)
        self.logoBackground_genPas.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 250))
        self.logoBackground_genPas.setProperty("class", "logoBackground_genPas")
        self.label_genPas = QtWidgets.QLabel(self.centralwidget)
        self.label_genPas.setGeometry(QtCore.QRect( round((MainWindow.width() - 560) / 2 ), 30, 560, 150))
        self.label_genPas.setPixmap(QtGui.QPixmap("../images/ezPassLogo.PNG"))
        self.label_genPas.setScaledContents(True)
        self.label_genPas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_genPas.setObjectName("label_genPas")
        self.label_genPas.setProperty("class", "label_logo")

        self.layoutWidget_1_genPas = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_1_genPas.setGeometry(QtCore.QRect(0, self.logoBackground_genPas.height() - 30, MainWindow.width(), 100)) 
        self.layoutWidget_1_genPas.setProperty("class", "navBar_genPas")

        self.HomeBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.HomeBtn_genPas.setProperty("class", "navBar_btn")
        self.VaultBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.VaultBtn_genPas.setProperty("class", "navBar_btn")
        self.SettingsBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.SettingsBtn_genPas.setProperty("class", "navBar_btn")
        self.AboutUsBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.AboutUsBtn_genPas.setProperty("class", "navBar_btn")
        self.dummyLabel_3_genPas = QtWidgets.QLabel(self.layoutWidget_1_genPas)
        self.dummyLabel_3_genPas.setProperty("class", "QLabel_genPas")
        self.dummyLabel_4_genPas = QtWidgets.QLabel(self.layoutWidget_1_genPas)
        self.dummyLabel_4_genPas.setProperty("class", "QLabel_genPas")

        self.navBar_genPas = QtWidgets.QHBoxLayout(self.layoutWidget_1_genPas)
        self.navBar_genPas.addWidget(self.HomeBtn_genPas)
        self.navBar_genPas.addWidget(self.VaultBtn_genPas)
        self.navBar_genPas.addWidget(self.SettingsBtn_genPas)
        self.navBar_genPas.addWidget(self.AboutUsBtn_genPas)
        self.navBar_genPas.addWidget(self.dummyLabel_3_genPas)
        self.navBar_genPas.addWidget(self.dummyLabel_4_genPas)

        

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
        self.chromeButton_genPas.setText(_translate("MainWindow", "Google Chrome"))
        self.FireFoxButton_genPas.setText(_translate("MainWindow", "FireFox"))
        self.MicrosoftEdgeButton_genPas.setText(_translate("MainWindow", "Microsoft Edge"))
        self.OperaButton_genPas.setText(_translate("MainWindow", "Opera"))
        self.HomeBtn_genPas.setText(_translate("MainWindow", "Home"))
        self.VaultBtn_genPas.setText(_translate("MainWindow", "Vault"))
        self.SettingsBtn_genPas.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_genPas.setText(_translate("MainWindow", "About Us"))
        self.label_selectBrowser.setText(_translate("MainWindow", "1. Select browser"))
        self.genPwd_genPas.setText(_translate("MainWindow", "Generate Password"))
        self.comboBox_Number_2_genPas.setItemText(0, _translate("MainWindow", "Number of words"))
        self.comboBox_Number_2_genPas.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_Number_2_genPas.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_Number_2_genPas.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_Number_2_genPas.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_Number_2_genPas.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_Number_3_genPas.setItemText(0, _translate("MainWindow", "Preference(s)"))
        self.dummyLabel_1_genPas.setText(_translate("MainWindow", ""))
        self.label_selectPreference_genPas.setText(_translate("MainWindow", "2. Select number of words & Preferences"))
        self.dummyLabel_2.setText(_translate("MainWindow", ""))
        self.dummyLabel_3_genPas.setText(_translate("MainWindow", ""))
        self.dummyLabel_4_genPas.setText(_translate("MainWindow", ""))
        self.label_Title_genPas.setText(_translate("MainWindow", "Generate Passphrase"))
        self.label_genPas.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.styleSheet = """
         .QPushButton_genPas {
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
        .QPushButton_genPas:hover {
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        .QPushButton_genPas:active {
            position:relative;
            top:1px;
        }

        .btn {
            border-radius: 30px;
        }

        .QGroupBox_genPas {
            background-color:#34363a;
            border: none;
        }

        .QLabel_genPas {
            color:#34363a; 
            background-color:#d2c15d;
        }

        .containers_genPas {
            background-color: #d2c15d;
            padding-bottom: 20px;
            border-radius:50px;
            border:2px solid #34363a;
        }

        .comboBox_genPas{
            background-color:#34363a;
            color:#d2c15d;
            font-size: 20px;
            padding-top: 5px;
            padding-bottom: 5px;
            padding-left: 10px;
        }

        .comboBox_genPas::down-arrow{
            image: url(../images/icons8-sort-down-100.png);
        }

        QMainWindow{
            background-color: #34363a;
        }

        .label_Title_genPas {
            font-size: 30px;
            color: #d2c15d;
            background-color:#34363a;
        }

        .label_logo {
            border: none;
        }

        .logoBackground_genPas {
            background-color: #454547;
         }

        .navBar_btn {
            color: #34363a;
            background-color: #d2c15d;
            border: none;
            text-align: left;
            font-size: 30px;
        }

        .navBar_btn:hover {
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        .navBar_btn:active {
            position:relative;
            top:1px;
        }

        .navBar_genPas {
            background-color: #d2c15d;
        }
    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
