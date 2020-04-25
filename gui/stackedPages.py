# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import prototype3 as p3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), MainWindow.height()))
        self.page_Home = QtWidgets.QWidget()
        self.page_Home.setObjectName("home page") 
        self.groupBox_Home = QtWidgets.QGroupBox(self.page_Home)
        self.groupBox_Home.setGeometry(QtCore.QRect(0, round(self.stackedWidget.height() * 0.3), self.stackedWidget.width(), round(self.stackedWidget.height() * 0.7)))
        self.groupBox_Home.setStyleSheet("")
        self.groupBox_Home.setObjectName("groupBox_Home")

        self.backgroundWidget_Home = QtWidgets.QLabel(self.groupBox_Home)
        self.backgroundWidget_Home.setGeometry(0, 0, self.groupBox_Home.width(), self.groupBox_Home.height())
        self.backgroundWidget_Home.setStyleSheet(" background-color: #d2c15d;")
 
        self.pbHeight_Home = round(self.groupBox_Home.height() * 0.28)
        self.pbWidth_Home = self.groupBox_Home.width() - 100;

        self.layoutWidget_2_Home = QtWidgets.QWidget(self.groupBox_Home)
        self.layoutWidget_2_Home.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth_Home) / 2), 10, self.pbWidth_Home, self.pbHeight_Home))
        self.layoutWidget_2_Home.setObjectName("layoutWidget_2_Home")
        self.layoutWidget_2_Home.setProperty("class", "layout_Background")
        self.horizontalLayout_GenPass_Home = QtWidgets.QHBoxLayout(self.layoutWidget_2_Home)
        self.horizontalLayout_GenPass_Home.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_GenPass_Home.setObjectName("horizontalLayout_GenPass_Home")
        self.pushButton_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.pushButton_Home.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth_Home) / 2), 10, self.pbWidth_Home, self.pbHeight_Home))
        self.pushButton_Home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_Home.setStyleSheet("")
        self.pushButton_Home.setText("")
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.pushButton_Home.clicked.connect(self.genPasPg)
        self.pushButton_Home.setProperty("class", "btn-style")
        self.verticalLayout_7_Home = QtWidgets.QVBoxLayout()
        self.verticalLayout_7_Home.setObjectName("verticalLayout_7_Home")
        self.label_genPwd_Home = QtWidgets.QLabel(self.layoutWidget_2_Home)
        self.label_genPwd_Home.setStyleSheet("")
        self.label_genPwd_Home.setObjectName("label_genPwd_Home")
        self.verticalLayout_7_Home.addWidget(self.label_genPwd_Home)
        self.label_genPwdDescription_Home = QtWidgets.QLabel(self.layoutWidget_2_Home)
        self.label_genPwdDescription_Home.setStyleSheet("")
        self.label_genPwdDescription_Home.setObjectName("label_genPwdDescription_Home")
        self.verticalLayout_7_Home.addWidget(self.label_genPwdDescription_Home)
        self.horizontalLayout_GenPass_Home.addLayout(self.verticalLayout_7_Home)
        self.dummy_label1_Home = QtWidgets.QLabel(self.layoutWidget_2_Home)
        self.dummy_label1_Home.setText("")
        self.dummy_label1_Home.setObjectName("dummy_label1_Home")
        self.horizontalLayout_GenPass_Home.addWidget(self.dummy_label1_Home)
        self.buttonPixmap_Gen_Home = QtWidgets.QLabel(self.layoutWidget_2_Home)
        self.buttonPixmap_Gen_Home.setText("")
        self.buttonPixmap_Gen_Home.setPixmap(QtGui.QPixmap("../images/generate_password.jpg"))
        self.buttonPixmap_Gen_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPixmap_Gen_Home.setObjectName("buttonPixmap_Gen_Home")
        self.horizontalLayout_GenPass_Home.addWidget(self.buttonPixmap_Gen_Home)

        self.layoutWidget_Home = QtWidgets.QWidget(self.groupBox_Home)
        self.layoutWidget_Home.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth_Home) / 2), self.pbHeight_Home + 20, self.pbWidth_Home, self.pbHeight_Home))
        self.layoutWidget_Home.setObjectName("layoutWidget_Home")
        self.layoutWidget_Home.setProperty("class", "layout_Background")
        self.horizontalLayout_vault_Home = QtWidgets.QHBoxLayout(self.layoutWidget_Home)
        self.horizontalLayout_vault_Home.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_vault_Home.setObjectName("horizontalLayout_vault_Home")
        self.pushButton_2_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.pushButton_2_Home.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth_Home) / 2), self.pbHeight_Home + 20, self.pbWidth_Home, self.pbHeight_Home))
        self.pushButton_2_Home.setStyleSheet("")
        self.pushButton_2_Home.setProperty("class", "btn-style")
        self.pushButton_2_Home.setText("")
        self.pushButton_2_Home.setObjectName("pushButton_2_Home")
        self.pushButton_2_Home.clicked.connect(self.vaultPg)
        self.verticalLayout_2_Home = QtWidgets.QVBoxLayout()
        self.verticalLayout_2_Home.setObjectName("verticalLayout_2_Home")
        self.label_vault_Home = QtWidgets.QLabel(self.layoutWidget_Home)
        self.label_vault_Home.setStyleSheet("")
        self.label_vault_Home.setObjectName("label_vault_Home")
        self.verticalLayout_2_Home.addWidget(self.label_vault_Home)
        self.label_vaultDescription_Home = QtWidgets.QLabel(self.layoutWidget_Home)
        self.label_vaultDescription_Home.setStyleSheet("")
        self.label_vaultDescription_Home.setObjectName("label_vaultDescription_Home")
        self.verticalLayout_2_Home.addWidget(self.label_vaultDescription_Home)
        self.horizontalLayout_vault_Home.addLayout(self.verticalLayout_2_Home)
        self.dummy_label2_Home = QtWidgets.QLabel(self.layoutWidget_Home)
        self.dummy_label2_Home.setStyleSheet("")
        self.dummy_label2_Home.setText("")
        self.dummy_label2_Home.setObjectName("dummy_label2_Home")
        self.horizontalLayout_vault_Home.addWidget(self.dummy_label2_Home)
        self.buttonPixmap_Vault_Home = QtWidgets.QLabel(self.layoutWidget_Home)
        self.buttonPixmap_Vault_Home.setText("")
        self.buttonPixmap_Vault_Home.setPixmap(QtGui.QPixmap("../images/smaller_vault.png"))
        self.buttonPixmap_Vault_Home.setScaledContents(True)
        self.buttonPixmap_Vault_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPixmap_Vault_Home.setObjectName("buttonPixmap_Vault_Home")
        self.horizontalLayout_vault_Home.addWidget(self.buttonPixmap_Vault_Home)

        self.layoutWidget_3_Home = QtWidgets.QWidget(self.groupBox_Home)
        self.layoutWidget_3_Home.setGeometry(QtCore.QRect(round((MainWindow.width() - self.pbWidth_Home) / 2), self.pbHeight_Home * 2 + 30, self.pbWidth_Home, self.pbHeight_Home))
        self.layoutWidget_3_Home.setObjectName("layoutWidget_3_Home")
        self.layoutWidget_3_Home.setProperty("class", "layout_Background")
        self.horizontalLayout_audit_Home = QtWidgets.QHBoxLayout(self.layoutWidget_3_Home)
        self.horizontalLayout_audit_Home.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_audit_Home.setObjectName("horizontalLayout_audit_Home")
        self.pushButton_3_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.pushButton_3_Home.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth_Home) / 2), self.pbHeight_Home * 2 + 30, self.pbWidth_Home, self.pbHeight_Home))
        self.pushButton_3_Home.setStyleSheet("")
        self.pushButton_3_Home.setProperty("class", "btn-style")
        self.pushButton_3_Home.setText("")
        self.pushButton_3_Home.setObjectName("pushButton_3_Home")
        self.pushButton_3_Home.clicked.connect(self.auditPg)
        self.verticalLayout_3_Home = QtWidgets.QVBoxLayout()
        self.verticalLayout_3_Home.setObjectName("verticalLayout_3_Home")
        self.label_audit_Home = QtWidgets.QLabel(self.layoutWidget_3_Home)
        self.label_audit_Home.setStyleSheet("")
        self.label_audit_Home.setObjectName("label_audit_Home")
        self.verticalLayout_3_Home.addWidget(self.label_audit_Home)
        self.label_auditDescription_Home = QtWidgets.QLabel(self.layoutWidget_3_Home)
        self.label_auditDescription_Home.setStyleSheet("")
        self.label_auditDescription_Home.setObjectName("label_auditDescription_Home")
        self.verticalLayout_3_Home.addWidget(self.label_auditDescription_Home)
        self.horizontalLayout_audit_Home.addLayout(self.verticalLayout_3_Home)
        self.dummy_label3_Home = QtWidgets.QLabel(self.layoutWidget_3_Home)
        self.dummy_label3_Home.setStyleSheet("")
        self.dummy_label3_Home.setText("")
        self.dummy_label3_Home.setObjectName("dummy_label3_Home")
        self.horizontalLayout_audit_Home.addWidget(self.dummy_label3_Home)
        self.buttonPixmap_audit_Home = QtWidgets.QLabel(self.layoutWidget_3_Home)
        self.buttonPixmap_audit_Home.setText("")
        self.buttonPixmap_audit_Home.setPixmap(QtGui.QPixmap("../images/security_Audit.jpg"))
        self.buttonPixmap_audit_Home.setObjectName("buttonPixmap_audit_Home")
        self.buttonPixmap_audit_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_audit_Home.addWidget(self.buttonPixmap_audit_Home)

        self.logoBackground_Home = QtWidgets.QLabel(self.page_Home)
        self.logoBackground_Home.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), 250))
        self.logoBackground_Home.setProperty("class", "logoBackground_Home")
        self.label_Home = QtWidgets.QLabel(self.page_Home)
        self.label_Home.setGeometry(QtCore.QRect( round((MainWindow.width() - 560) / 2 ), 30, 560, 150))
        self.label_Home.setPixmap(QtGui.QPixmap("../images/ezPassLogo.PNG"))
        self.label_Home.setScaledContents(True)
        self.label_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Home.setObjectName("label_Home")
        self.label_Home.setProperty("class", "label_logo")

        self.settings_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.settings_Home.setGeometry(QtCore.QRect(MainWindow.width() - 370, 565, 160, 35))
        self.settings_Home.setStyleSheet("color: #34363a; background-color: #d2c15d; font-size: 20px")
        self.aboutUs_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.aboutUs_Home.setGeometry(QtCore.QRect(MainWindow.width() - 210, 565, 160, 35))
        self.aboutUs_Home.setStyleSheet("color: #34363a; background-color: #d2c15d; font-size: 20px")

        self.label_14_Home = QtWidgets.QLabel(self.page_Home)
        self.label_14_Home.setGeometry(QtCore.QRect(0, self.logoBackground_Home.y()+ 215, MainWindow.width(), 55))
        self.label_14_Home.setStyleSheet("font-size: 30px")
        self.label_14_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14_Home.setObjectName("label_14_Home")

        self.stackedWidget.addWidget(self.page_Home)

        self.page_genPas = QtWidgets.QWidget()
        self.page_genPas.setObjectName("page_genPas")
        self.groupBox_genPas = QtWidgets.QGroupBox(self.page_genPas)
        self.groupBox_genPas.setGeometry(QtCore.QRect(round((self.stackedWidget.width() - 1300) / 2), round((self.stackedWidget.height() - 450 ) / 7 *6), 1300, 450))
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
        self.label_Title_genPas = QtWidgets.QLabel(self.page_genPas)
        self.label_Title_genPas.setProperty("class", "label_Title_genPas")
        self.label_Title_genPas.setGeometry(QtCore.QRect(self.groupBox_genPas.x() + 20, self.groupBox_genPas.y() - 70, 300, 70))

        #buttons
        self.chromeButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon1_genPas = QtGui.QIcon()
        icon1_genPas.addPixmap(QtGui.QPixmap("../images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton_genPas.setIcon(icon1_genPas)
        self.chromeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton_genPas.setObjectName("chromeButton_genPas")
        self.chromeButton_genPas.setProperty("class", "QPushButton_genPas")
        self.FireFoxButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon2_genPas = QtGui.QIcon()
        icon2_genPas.addPixmap(QtGui.QPixmap("../images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton_genPas.setIcon(icon2_genPas)
        self.FireFoxButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton_genPas.setObjectName("FireFoxButton_genPas")
        self.FireFoxButton_genPas.setProperty("class", "QPushButton_genPas")
        self.MicrosoftEdgeButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon3_genPas = QtGui.QIcon()
        icon3_genPas.addPixmap(QtGui.QPixmap("../images/icons8-microsoft-edge-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrosoftEdgeButton_genPas.setIcon(icon3_genPas)
        self.MicrosoftEdgeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.MicrosoftEdgeButton_genPas.setObjectName("MicrosoftEdgeButton_genPas")
        self.MicrosoftEdgeButton_genPas.setProperty("class", "QPushButton_genPas")
        self.OperaButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon4_genPas = QtGui.QIcon()
        icon4_genPas.addPixmap(QtGui.QPixmap("../images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OperaButton_genPas.setIcon(icon4_genPas)
        self.OperaButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.OperaButton_genPas.setObjectName("OperaButton_genPas")
        self.OperaButton_genPas.setProperty("class", "QPushButton_genPas")
        
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
        self.genPwd_genPas.setProperty("class", "btn")
        self.genPwd_genPas.setCheckable(False)
        self.genPwd_genPas.setChecked(False)
        self.genPwd_genPas.setFlat(False)
        self.genPwd_genPas.setObjectName("genPwd_genPas")
        
        self.comboBox_Number_2_genPas = QtWidgets.QComboBox(self.groupBox_genPas)
        self.comboBox_Number_2_genPas.setEnabled(True)
        self.comboBox_Number_2_genPas.setObjectName("comboBox_Number_2_genPas")
        self.comboBox_Number_2_genPas.setProperty("class", "comboBox_genPas")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        
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
        
        self.dummyLabel_2_genPas = QtWidgets.QLabel(self.groupBox_genPas)
        self.dummyLabel_2_genPas.setObjectName("dummyLabel_2")
        self.dummyLabel_2_genPas.setProperty("class", "QLabel_genPas")

        self.gridLayout_2_genPas.addWidget(self.label_selectPreference_genPas, 0, 0, 1, 4)
        self.gridLayout_2_genPas.addWidget(self.comboBox_Number_2_genPas, 1, 1, 1, 3)
        self.gridLayout_2_genPas.addWidget(self.comboBox_Number_3_genPas, 2, 1, 1, 3)
        self.gridLayout_2_genPas.addWidget(self.dummyLabel_1_genPas, 1, 0, 1, 1)
        self.gridLayout_2_genPas.addWidget(self.dummyLabel_2_genPas, 1, 4, 1, 1)
        self.gridLayout_2_genPas.addWidget(self.genPwd_genPas, 3, 2, 1, 1)
        self.verticalLayout_genPas.addWidget(self.container_2_genPas)

        self.logoBackground_genPas = QtWidgets.QLabel(self.page_genPas)
        self.logoBackground_genPas.setGeometry(QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
        self.logoBackground_genPas.setProperty("class", "logoBackground_genPas")
        self.label_genPas = QtWidgets.QLabel(self.centralwidget)
        self.label_genPas.setGeometry(QtCore.QRect( round((self.stackedWidget.width() - 560) / 2 ), 30, 560, 150))
        self.label_genPas.setPixmap(QtGui.QPixmap("../images/ezPassLogo.PNG"))
        self.label_genPas.setScaledContents(True)
        self.label_genPas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_genPas.setObjectName("label_genPas")
        self.label_genPas.setProperty("class", "label_logo")

        self.layoutWidget_1_genPas = QtWidgets.QWidget(self.page_genPas)
        self.layoutWidget_1_genPas.setGeometry(QtCore.QRect(0, self.logoBackground_genPas.height() - 30, self.stackedWidget.width(), 100)) 
        self.layoutWidget_1_genPas.setProperty("class", "navBar_genPas")

        self.HomeBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.HomeBtn_genPas.setProperty("class", "navBar_btn")
        self.HomeBtn_genPas.clicked.connect(self.homePg)
        self.VaultBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.VaultBtn_genPas.setProperty("class", "navBar_btn")
        self.VaultBtn_genPas.clicked.connect(self.vaultPg)
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

        self.stackedWidget.addWidget(self.page_genPas)

        self.page_vault = QtWidgets.QWidget()
        self.page_vault.setObjectName("page_vault")
        self.groupBox_vault = QtWidgets.QGroupBox(self.page_vault)
        self.groupBox_vault.setGeometry(QtCore.QRect(round((self.stackedWidget.width() - 1300) / 2), round((self.stackedWidget.height() - 450 ) / 7 *6), 1300, 450))
        self.groupBox_vault.setObjectName("groupBox_vault")
        self.groupBox_vault.setProperty("class", "QGroupBox_genPas")
        self.verticalLayout_vault = QtWidgets.QVBoxLayout(self.groupBox_vault)
        self.verticalLayout_vault.setObjectName("verticalLayout_vault")
        self.container_1_vault = QtWidgets.QWidget()
        self.container_1_vault.setProperty("class", "containers_genPas")
        self.gridLayout_vault = QtWidgets.QGridLayout(self.container_1_vault)
        self.gridLayout_vault.setContentsMargins(25, 10, 15, 10)
        self.gridLayout_vault.setHorizontalSpacing(30)
        self.gridLayout_vault.setVerticalSpacing(10)
        self.gridLayout_vault.setObjectName("gridLayout_vault")
        self.label_Title_vault = QtWidgets.QLabel(self.page_vault)
        self.label_Title_vault.setProperty("class", "label_Title_genPas")
        self.label_Title_vault.setGeometry(QtCore.QRect(self.groupBox_vault.x() + 20, self.groupBox_vault.y() - 70, 300, 70))

        self.logoBackground_vault = QtWidgets.QLabel(self.page_vault)
        self.logoBackground_vault.setGeometry(QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
        self.logoBackground_vault.setProperty("class", "logoBackground_genPas")
        self.label_vault = QtWidgets.QLabel(self.centralwidget)
        self.label_vault.setGeometry(QtCore.QRect( round((self.stackedWidget.width() - 560) / 2 ), 30, 560, 150))
        self.label_vault.setPixmap(QtGui.QPixmap("../images/ezPassLogo.PNG"))
        self.label_vault.setScaledContents(True)
        self.label_vault.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vault.setObjectName("label_vault")
        self.label_vault.setProperty("class", "label_logo")

        self.layoutWidget_1_vault = QtWidgets.QWidget(self.page_vault)
        self.layoutWidget_1_vault.setGeometry(QtCore.QRect(0, self.logoBackground_vault.height() - 30, self.stackedWidget.width(), 100)) 
        self.layoutWidget_1_vault.setProperty("class", "navBar_genPas")

        self.HomeBtn_vault = QtWidgets.QPushButton(self.layoutWidget_1_vault)
        self.HomeBtn_vault.setProperty("class", "navBar_btn")
        self.HomeBtn_vault.clicked.connect(self.homePg)
        self.SettingsBtn_vault = QtWidgets.QPushButton(self.layoutWidget_1_vault)
        self.SettingsBtn_vault.setProperty("class", "navBar_btn")
        self.AboutUsBtn_vault = QtWidgets.QPushButton(self.layoutWidget_1_vault)
        self.AboutUsBtn_vault.setProperty("class", "navBar_btn")
        self.dummyLabel_3_vault = QtWidgets.QLabel(self.layoutWidget_1_vault)
        self.dummyLabel_3_vault.setProperty("class", "QLabel_genPas")
        self.dummyLabel_4_vault = QtWidgets.QLabel(self.layoutWidget_1_vault)
        self.dummyLabel_4_vault.setProperty("class", "QLabel_genPas")

        self.navBar_vault = QtWidgets.QHBoxLayout(self.layoutWidget_1_vault)
        self.navBar_vault.addWidget(self.HomeBtn_vault)
        self.navBar_vault.addWidget(self.SettingsBtn_vault)
        self.navBar_vault.addWidget(self.AboutUsBtn_vault)
        self.navBar_vault.addWidget(self.dummyLabel_3_vault)
        self.navBar_vault.addWidget(self.dummyLabel_4_vault)

        self.stackedWidget.addWidget(self.page_vault)

        self.page_audit = QtWidgets.QWidget()
        self.page_audit.setObjectName("page_audit")
        self.groupBox_audit = QtWidgets.QGroupBox(self.page_audit)
        self.groupBox_audit.setGeometry(QtCore.QRect(round((self.stackedWidget.width() - 1300) / 2), round((self.stackedWidget.height() - 450 ) / 7 *6), 1300, 450))
        self.groupBox_audit.setObjectName("groupBox_audit")
        self.groupBox_audit.setProperty("class", "QGroupBox_genPas")
        self.verticalLayout_audit = QtWidgets.QVBoxLayout(self.groupBox_audit)
        self.verticalLayout_audit.setObjectName("verticalLayout_audit")
        self.container_1_audit = QtWidgets.QWidget()
        self.container_1_audit.setProperty("class", "containers_genPas")
        self.gridLayout_audit = QtWidgets.QGridLayout(self.container_1_audit)
        self.gridLayout_audit.setContentsMargins(25, 10, 15, 10)
        self.gridLayout_audit.setHorizontalSpacing(30)
        self.gridLayout_audit.setVerticalSpacing(10)
        self.gridLayout_audit.setObjectName("gridLayout_audit")
        self.label_Title_audit = QtWidgets.QLabel(self.page_audit)
        self.label_Title_audit.setProperty("class", "label_Title_genPas")
        self.label_Title_audit.setGeometry(QtCore.QRect(self.groupBox_audit.x() + 20, self.groupBox_audit.y() - 70, 300, 70))

        self.logoBackground_audit = QtWidgets.QLabel(self.page_audit)
        self.logoBackground_audit.setGeometry(QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
        self.logoBackground_audit.setProperty("class", "logoBackground_genPas")
        self.label_audit = QtWidgets.QLabel(self.centralwidget)
        self.label_audit.setGeometry(QtCore.QRect( round((self.stackedWidget.width() - 560) / 2 ), 30, 560, 150))
        self.label_audit.setPixmap(QtGui.QPixmap("../images/ezPassLogo.PNG"))
        self.label_audit.setScaledContents(True)
        self.label_audit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_audit.setObjectName("label_audit")
        self.label_audit.setProperty("class", "label_logo")

        self.layoutWidget_1_audit = QtWidgets.QWidget(self.page_audit)
        self.layoutWidget_1_audit.setGeometry(QtCore.QRect(0, self.logoBackground_audit.height() - 30, self.stackedWidget.width(), 100)) 
        self.layoutWidget_1_audit.setProperty("class", "navBar_genPas")

        self.HomeBtn_audit = QtWidgets.QPushButton(self.layoutWidget_1_audit)
        self.HomeBtn_audit.setProperty("class", "navBar_btn")
        self.HomeBtn_audit.clicked.connect(self.homePg)
        self.VaultBtn_audit = QtWidgets.QPushButton(self.layoutWidget_1_audit)
        self.VaultBtn_audit.setProperty("class", "navBar_btn")
        self.VaultBtn_audit.clicked.connect(self.vaultPg)
        self.SettingsBtn_audit = QtWidgets.QPushButton(self.layoutWidget_1_audit)
        self.SettingsBtn_audit.setProperty("class", "navBar_btn")
        self.AboutUsBtn_audit = QtWidgets.QPushButton(self.layoutWidget_1_audit)
        self.AboutUsBtn_audit.setProperty("class", "navBar_btn")
        self.dummyLabel_3_audit = QtWidgets.QLabel(self.layoutWidget_1_audit)
        self.dummyLabel_3_audit.setProperty("class", "QLabel_genPas")
        self.dummyLabel_4_audit = QtWidgets.QLabel(self.layoutWidget_1_audit)
        self.dummyLabel_4_audit.setProperty("class", "QLabel_genPas")

        self.navBar_audit = QtWidgets.QHBoxLayout(self.layoutWidget_1_audit)
        self.navBar_audit.addWidget(self.HomeBtn_audit)
        self.navBar_audit.addWidget(self.VaultBtn_audit)
        self.navBar_audit.addWidget(self.SettingsBtn_audit)
        self.navBar_audit.addWidget(self.AboutUsBtn_audit)
        self.navBar_audit.addWidget(self.dummyLabel_3_audit)
        self.navBar_audit.addWidget(self.dummyLabel_4_audit)

        self.stackedWidget.addWidget(self.page_audit)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EzPass"))
        self.groupBox_Home.setTitle(_translate("MainWindow", ""))
        self.label_genPwd_Home.setText(_translate("MainWindow", "1. Generate Passphrase"))
        self.label_genPwdDescription_Home.setText(_translate("MainWindow", "Obtain a password using our simple but secure algorithm "))
        self.label_vault_Home.setText(_translate("MainWindow", "2. Access my vault"))
        self.label_vaultDescription_Home.setText(_translate("MainWindow", "View & add passwords into your vault"))
        self.label_audit_Home.setText(_translate("MainWindow", "3. Security Audit"))
        self.label_auditDescription_Home.setText(_translate("MainWindow", "Assess the security of the passwords in your vault"))
        self.label_14_Home.setText(_translate("MainWindow", "Welcome, what would you like to do?"))
        self.settings_Home.setText(_translate("MainWindow", "Settings"))
        self.aboutUs_Home.setText(_translate("MainWindow", "About Us"))

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
        self.dummyLabel_2_genPas.setText(_translate("MainWindow", ""))
        self.dummyLabel_3_genPas.setText(_translate("MainWindow", ""))
        self.dummyLabel_4_genPas.setText(_translate("MainWindow", ""))
        self.label_Title_genPas.setText(_translate("MainWindow", "Generate Passphrase"))
        self.label_genPas.setText(_translate("MainWindow", ""))

        self.HomeBtn_vault.setText(_translate("MainWindow", "Home"))
        self.SettingsBtn_vault.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_vault.setText(_translate("MainWindow", "About Us"))

        self.HomeBtn_audit.setText(_translate("MainWindow", "Home"))
        self.VaultBtn_audit.setText(_translate("MainWindow", "Vault"))
        self.SettingsBtn_audit.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_audit.setText(_translate("MainWindow", "About Us"))
        
    def homePg(self):
        self.stackedWidget.setCurrentIndex(0)

    def genPasPg(self):
        self.stackedWidget.setCurrentIndex(1)

    def vaultPg(self):
        self.stackedWidget.setCurrentIndex(2)

    def auditPg(self):
        self.stackedWidget.setCurrentIndex(3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.styleSheet = """
        QPushButton {
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color: #ffffff;
            border:2px solid #34363a;  
        }
        QPushButton:hover {
            border: 5px solid #6da4fc;
        }
        QPushButton:active {
            position:relative;
            top:1px;
        }

        QLabel {
           background-color: #34363a;
           color:#d2c15d;
           font-size: 25px;
        }

        .btn-style {
           background-color: transparent;
        }

        QHBoxLayout {
           background-color: #34363a;
        }

        .layout_Background {
           background-color: #34363a;
        }

        .logoBackground_Home {
            background-color: #454547;
         }

        .QPushButton_genPas {
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color:#34363a;
            border-radius:39px;
            border:2px solid #34363a;
            color:#d2c15d;
            font-family:Trebuchet MS;
            font-size:19px;
            font-weight:bold;
            padding:20px 45px;
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
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color:#34363a;
            border:2px solid #34363a;
            color:#d2c15d;
            font-family:Trebuchet MS;
            font-size:19px;
            font-weight:bold;
            padding:20px 14px;
            text-decoration:none;
            border-radius: 30px;
        }

        .btn:hover {
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        .btn:active {
            position:relative;
            top:1px;
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
