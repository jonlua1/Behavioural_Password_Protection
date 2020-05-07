# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#import prototype3 as p3
from customWidget import OnOffWidget
from dialogBox import Ui_Dialog
from generator import generate_password


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/lock_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(
            0, 0, MainWindow.width(), MainWindow.height()))
        self.page_Home = QtWidgets.QWidget()
        self.page_Home.setObjectName("home page")
        self.groupBox_Home = QtWidgets.QGroupBox(self.page_Home)
        self.groupBox_Home.setGeometry(QtCore.QRect(0, round(self.stackedWidget.height(
        ) * 0.3), self.stackedWidget.width(), round(self.stackedWidget.height() * 0.7)))
        self.groupBox_Home.setStyleSheet("")
        self.groupBox_Home.setObjectName("groupBox_Home")

        self.backgroundWidget_Home = QtWidgets.QLabel(self.groupBox_Home)
        self.backgroundWidget_Home.setGeometry(
            0, 0, self.groupBox_Home.width(), self.groupBox_Home.height())
        self.backgroundWidget_Home.setStyleSheet(" background-color: #d2c15d;")

        self.pbHeight_Home = round(self.groupBox_Home.height() * 0.28)
        self.pbWidth_Home = self.groupBox_Home.width() - 100

        self.layoutWidget_2_Home = QtWidgets.QWidget(self.groupBox_Home)
        self.layoutWidget_2_Home.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - self.pbWidth_Home) / 2), 10, self.pbWidth_Home, self.pbHeight_Home))
        self.layoutWidget_2_Home.setObjectName("layoutWidget_2_Home")
        self.layoutWidget_2_Home.setProperty("class", "layout_Background")
        self.horizontalLayout_GenPass_Home = QtWidgets.QHBoxLayout(
            self.layoutWidget_2_Home)
        self.horizontalLayout_GenPass_Home.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_GenPass_Home.setObjectName(
            "horizontalLayout_GenPass_Home")
        self.pushButton_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.pushButton_Home.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - self.pbWidth_Home) / 2), 10, self.pbWidth_Home, self.pbHeight_Home))
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
        self.label_genPwdDescription_Home = QtWidgets.QLabel(
            self.layoutWidget_2_Home)
        self.label_genPwdDescription_Home.setStyleSheet("")
        self.label_genPwdDescription_Home.setObjectName(
            "label_genPwdDescription_Home")
        self.verticalLayout_7_Home.addWidget(self.label_genPwdDescription_Home)
        self.horizontalLayout_GenPass_Home.addLayout(
            self.verticalLayout_7_Home)
        self.dummy_label1_Home = QtWidgets.QLabel(self.layoutWidget_2_Home)
        self.dummy_label1_Home.setText("")
        self.dummy_label1_Home.setObjectName("dummy_label1_Home")
        self.horizontalLayout_GenPass_Home.addWidget(self.dummy_label1_Home)
        self.buttonPixmap_Gen_Home = QtWidgets.QLabel(self.layoutWidget_2_Home)
        self.buttonPixmap_Gen_Home.setText("")
        self.buttonPixmap_Gen_Home.setPixmap(
            QtGui.QPixmap("images/generate_password.jpg"))
        self.buttonPixmap_Gen_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPixmap_Gen_Home.setObjectName("buttonPixmap_Gen_Home")
        self.horizontalLayout_GenPass_Home.addWidget(
            self.buttonPixmap_Gen_Home)

        self.layoutWidget_Home = QtWidgets.QWidget(self.groupBox_Home)
        self.layoutWidget_Home.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - self.pbWidth_Home) / 2), self.pbHeight_Home + 20, self.pbWidth_Home, self.pbHeight_Home))
        self.layoutWidget_Home.setObjectName("layoutWidget_Home")
        self.layoutWidget_Home.setProperty("class", "layout_Background")
        self.horizontalLayout_vault_Home = QtWidgets.QHBoxLayout(
            self.layoutWidget_Home)
        self.horizontalLayout_vault_Home.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_vault_Home.setObjectName(
            "horizontalLayout_vault_Home")
        self.pushButton_2_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.pushButton_2_Home.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - self.pbWidth_Home) / 2), self.pbHeight_Home + 20, self.pbWidth_Home, self.pbHeight_Home))
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
        self.label_vaultDescription_Home = QtWidgets.QLabel(
            self.layoutWidget_Home)
        self.label_vaultDescription_Home.setStyleSheet("")
        self.label_vaultDescription_Home.setObjectName(
            "label_vaultDescription_Home")
        self.verticalLayout_2_Home.addWidget(self.label_vaultDescription_Home)
        self.horizontalLayout_vault_Home.addLayout(self.verticalLayout_2_Home)
        self.dummy_label2_Home = QtWidgets.QLabel(self.layoutWidget_Home)
        self.dummy_label2_Home.setStyleSheet("")
        self.dummy_label2_Home.setText("")
        self.dummy_label2_Home.setObjectName("dummy_label2_Home")
        self.horizontalLayout_vault_Home.addWidget(self.dummy_label2_Home)
        self.buttonPixmap_Vault_Home = QtWidgets.QLabel(self.layoutWidget_Home)
        self.buttonPixmap_Vault_Home.setText("")
        self.buttonPixmap_Vault_Home.setPixmap(
            QtGui.QPixmap("images/smaller_vault.png"))
        self.buttonPixmap_Vault_Home.setScaledContents(True)
        self.buttonPixmap_Vault_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPixmap_Vault_Home.setObjectName("buttonPixmap_Vault_Home")
        self.horizontalLayout_vault_Home.addWidget(
            self.buttonPixmap_Vault_Home)

        self.layoutWidget_3_Home = QtWidgets.QWidget(self.groupBox_Home)
        self.layoutWidget_3_Home.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - self.pbWidth_Home) / 2), self.pbHeight_Home * 2 + 30, self.pbWidth_Home, self.pbHeight_Home))
        self.layoutWidget_3_Home.setObjectName("layoutWidget_3_Home")
        self.layoutWidget_3_Home.setProperty("class", "layout_Background")
        self.horizontalLayout_audit_Home = QtWidgets.QHBoxLayout(
            self.layoutWidget_3_Home)
        self.horizontalLayout_audit_Home.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_audit_Home.setObjectName(
            "horizontalLayout_audit_Home")
        self.pushButton_3_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.pushButton_3_Home.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - self.pbWidth_Home) / 2), self.pbHeight_Home * 2 + 30, self.pbWidth_Home, self.pbHeight_Home))
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
        self.label_auditDescription_Home = QtWidgets.QLabel(
            self.layoutWidget_3_Home)
        self.label_auditDescription_Home.setStyleSheet("")
        self.label_auditDescription_Home.setObjectName(
            "label_auditDescription_Home")
        self.verticalLayout_3_Home.addWidget(self.label_auditDescription_Home)
        self.horizontalLayout_audit_Home.addLayout(self.verticalLayout_3_Home)
        self.dummy_label3_Home = QtWidgets.QLabel(self.layoutWidget_3_Home)
        self.dummy_label3_Home.setStyleSheet("")
        self.dummy_label3_Home.setText("")
        self.dummy_label3_Home.setObjectName("dummy_label3_Home")
        self.horizontalLayout_audit_Home.addWidget(self.dummy_label3_Home)
        self.buttonPixmap_audit_Home = QtWidgets.QLabel(
            self.layoutWidget_3_Home)
        self.buttonPixmap_audit_Home.setText("")
        self.buttonPixmap_audit_Home.setPixmap(
            QtGui.QPixmap("images/security_Audit_adjust.jpg"))
        self.buttonPixmap_audit_Home.setObjectName("buttonPixmap_audit_Home")
        self.buttonPixmap_audit_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_audit_Home.addWidget(
            self.buttonPixmap_audit_Home)

        self.logoBackground_Home = QtWidgets.QLabel(self.page_Home)
        self.logoBackground_Home.setGeometry(
            QtCore.QRect(0, 0, MainWindow.width(), 250))
        self.logoBackground_Home.setProperty("class", "logoBackground_Home")
        self.label_Home = QtWidgets.QLabel(self.page_Home)
        self.label_Home.setGeometry(QtCore.QRect(
            round((MainWindow.width() - 560) / 2), 30, 560, 150))
        self.label_Home.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_Home.setScaledContents(True)
        self.label_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Home.setObjectName("label_Home")
        self.label_Home.setProperty("class", "label_logo")

        self.settings_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.settings_Home.setGeometry(QtCore.QRect(
            MainWindow.width() - 370, 565, 160, 35))
        self.settings_Home.setStyleSheet(
            "color: #34363a; background-color: #d2c15d; font-size: 20px")
        self.aboutUs_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.aboutUs_Home.setGeometry(QtCore.QRect(
            MainWindow.width() - 210, 565, 160, 35))
        self.aboutUs_Home.setStyleSheet(
            "color: #34363a; background-color: #d2c15d; font-size: 20px")

        self.label_14_Home = QtWidgets.QLabel(self.page_Home)
        self.label_14_Home.setGeometry(QtCore.QRect(
            0, self.logoBackground_Home.y() + 215, MainWindow.width(), 55))
        self.label_14_Home.setStyleSheet("font-size: 30px")
        self.label_14_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14_Home.setObjectName("label_14_Home")

        self.stackedWidget.addWidget(self.page_Home)
########################################################################################################
        self.page_genPas = QtWidgets.QWidget()
        self.page_genPas.setObjectName("page_genPas")
        self.groupBox_genPas = QtWidgets.QGroupBox(self.page_genPas)
        self.groupBox_genPas.setGeometry(QtCore.QRect(round((self.stackedWidget.width(
        ) - 1300) / 2), round((self.stackedWidget.height() - 450) / 7 * 6), 1300, 450))
        self.groupBox_genPas.setObjectName("groupBox_genPas")
        self.groupBox_genPas.setProperty("class", "QGroupBox_genPas")
        self.verticalLayout_genPas = QtWidgets.QVBoxLayout(
            self.groupBox_genPas)
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
        self.label_Title_genPas.setGeometry(QtCore.QRect(
            self.groupBox_genPas.x() + 20, self.groupBox_genPas.y() - 70, 300, 70))

       

        # buttons
        self.chromeButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon1_genPas = QtGui.QIcon()
        icon1_genPas.addPixmap(QtGui.QPixmap(
            "images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton_genPas.setIcon(icon1_genPas)
        self.chromeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton_genPas.setCheckable(True)
        self.chromeButton_genPas.setObjectName("chromeButton_genPas")
        self.chromeButton_genPas.setProperty("class", "QPushButton_genPas")
        self.FireFoxButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon2_genPas = QtGui.QIcon()
        icon2_genPas.addPixmap(QtGui.QPixmap(
            "images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton_genPas.setIcon(icon2_genPas)
        self.FireFoxButton_genPas.setCheckable(True)
        self.FireFoxButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton_genPas.setObjectName("FireFoxButton_genPas")
        self.FireFoxButton_genPas.setProperty("class", "QPushButton_genPas")
        self.MicrosoftEdgeButton_genPas = QtWidgets.QPushButton(
            self.groupBox_genPas)
        icon3_genPas = QtGui.QIcon()
        icon3_genPas.addPixmap(QtGui.QPixmap(
            "images/icons8-microsoft-edge-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrosoftEdgeButton_genPas.setIcon(icon3_genPas)
        self.MicrosoftEdgeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.MicrosoftEdgeButton_genPas.setCheckable(True)
        self.MicrosoftEdgeButton_genPas.setObjectName(
            "MicrosoftEdgeButton_genPas")
        self.MicrosoftEdgeButton_genPas.setProperty(
            "class", "QPushButton_genPas")
        self.OperaButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon4_genPas = QtGui.QIcon()
        icon4_genPas.addPixmap(QtGui.QPixmap(
            "images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OperaButton_genPas.setIcon(icon4_genPas)
        self.OperaButton_genPas.setCheckable(True)
        self.OperaButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.OperaButton_genPas.setObjectName("OperaButton_genPas")
        self.OperaButton_genPas.setProperty("class", "QPushButton_genPas")
       
        self.FireFoxButton_genPas.clicked.connect(self.appendToBtnList)
        self.chromeButton_genPas.clicked.connect(self.appendToBtnList)
        self.MicrosoftEdgeButton_genPas.clicked.connect(self.appendToBtnList)
        self.OperaButton_genPas.clicked.connect(self.appendToBtnList)

        #btn array to store buttons that are selected
        self.btnList = []

        self.label_selectBrowser = QtWidgets.QLabel(self.groupBox_genPas)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectBrowser.setFont(font)
        self.label_selectBrowser.setAutoFillBackground(False)
        self.label_selectBrowser.setObjectName("label_selectBrowser")
        self.label_selectBrowser.setProperty("class", "QLabel_genPas")

        self.gridLayout_genPas.addWidget(self.chromeButton_genPas, 1, 0, 1, 1)
        self.gridLayout_genPas.addWidget(self.FireFoxButton_genPas, 1, 1, 1, 1)
        self.gridLayout_genPas.addWidget(
            self.MicrosoftEdgeButton_genPas, 1, 3, 1, 1)
        self.gridLayout_genPas.addWidget(self.OperaButton_genPas, 1, 2, 1, 1)
        self.gridLayout_genPas.addWidget(self.label_selectBrowser, 0, 0, 1, 2)
        self.verticalLayout_genPas.addWidget(self.container_1_genPas)

        self.container_2_genPas = QtWidgets.QWidget()
        self.container_2_genPas.setProperty("class", "containers_genPas")
        self.gridLayout_2_genPas = QtWidgets.QGridLayout(
            self.container_2_genPas)
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
        self.genPwd_genPas.clicked.connect(self.genPassword)

        self.comboBox_Number_2_genPas = QtWidgets.QComboBox(
            self.groupBox_genPas)
        self.comboBox_Number_2_genPas.setEditText("Woaw")
        self.comboBox_Number_2_genPas.setEnabled(True)
        self.comboBox_Number_2_genPas.setObjectName("comboBox_Number_2_genPas")
        self.comboBox_Number_2_genPas.setProperty("class", "comboBox_genPas")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.currentIndexChanged.connect(self.appendToCBList_wordNo)

        self.comboBox_wordNo = ""

        self.comboBox_Number_3_genPas = QtWidgets.QComboBox(
            self.groupBox_genPas)
        self.comboBox_Number_3_genPas.setEnabled(True)
        self.comboBox_Number_3_genPas.setObjectName("comboBox_Number_3_genPas")
        self.comboBox_Number_3_genPas.addItem("")
        self.comboBox_Number_3_genPas.setProperty("class", "comboBox_genPas")

        self.dummyLabel_1_genPas = QtWidgets.QLabel(self.groupBox_genPas)
        self.dummyLabel_1_genPas.setObjectName("dummyLabel_1_genPas")
        self.dummyLabel_1_genPas.setProperty("class", "QLabel_genPas")

        self.label_selectPreference_genPas = QtWidgets.QLabel(
            self.groupBox_genPas)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectPreference_genPas.setFont(font)
        self.label_selectPreference_genPas.setAutoFillBackground(True)
        self.label_selectPreference_genPas.setObjectName(
            "label_selectPreference_genPas")
        self.label_selectPreference_genPas.setProperty(
            "class", "QLabel_genPas")

        self.dummyLabel_2_genPas = QtWidgets.QLabel(self.groupBox_genPas)
        self.dummyLabel_2_genPas.setObjectName("dummyLabel_2")
        self.dummyLabel_2_genPas.setProperty("class", "QLabel_genPas")

        self.gridLayout_2_genPas.addWidget(
            self.label_selectPreference_genPas, 0, 0, 1, 4)
        self.gridLayout_2_genPas.addWidget(
            self.comboBox_Number_2_genPas, 1, 1, 1, 3)
        self.gridLayout_2_genPas.addWidget(
            self.comboBox_Number_3_genPas, 2, 1, 1, 3)
        self.gridLayout_2_genPas.addWidget(
            self.dummyLabel_1_genPas, 1, 0, 1, 1)
        self.gridLayout_2_genPas.addWidget(
            self.dummyLabel_2_genPas, 1, 4, 1, 1)
        self.gridLayout_2_genPas.addWidget(self.genPwd_genPas, 3, 2, 1, 1)
        self.verticalLayout_genPas.addWidget(self.container_2_genPas)

        self.logoBackground_genPas = QtWidgets.QLabel(self.page_genPas)
        self.logoBackground_genPas.setGeometry(
            QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
        self.logoBackground_genPas.setProperty(
            "class", "logoBackground_genPas")
        self.label_genPas = QtWidgets.QLabel(self.page_genPas)
        self.label_genPas.setGeometry(QtCore.QRect(
            round((self.stackedWidget.width() - 560) / 2), 30, 560, 150))
        self.label_genPas.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_genPas.setScaledContents(True)
        self.label_genPas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_genPas.setObjectName("label_genPas")
        self.label_genPas.setProperty("class", "label_logo")

        self.layoutWidget_1_genPas = QtWidgets.QWidget(self.page_genPas)
        self.layoutWidget_1_genPas.setGeometry(QtCore.QRect(
            0, self.logoBackground_genPas.height() - 30, self.stackedWidget.width(), 100))
        self.layoutWidget_1_genPas.setProperty("class", "navBar_genPas")

        self.HomeBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_1_genPas)
        self.HomeBtn_genPas.setProperty("class", "navBar_btn")
        self.HomeBtn_genPas.clicked.connect(self.homePg)
        self.VaultBtn_genPas = QtWidgets.QPushButton(
            self.layoutWidget_1_genPas)
        self.VaultBtn_genPas.setProperty("class", "navBar_btn")
        self.VaultBtn_genPas.clicked.connect(self.vaultPg)
        self.SettingsBtn_genPas = QtWidgets.QPushButton(
            self.layoutWidget_1_genPas)
        self.SettingsBtn_genPas.setProperty("class", "navBar_btn")
        self.AboutUsBtn_genPas = QtWidgets.QPushButton(
            self.layoutWidget_1_genPas)
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
#########################################################################################
        self.page_vault = QtWidgets.QWidget()
        self.page_vault.setObjectName("page_vault")
        self.scrollArea_vault = QtWidgets.QScrollArea(self.page_vault)
        self.scrollArea_vault.setGeometry(QtCore.QRect(
            0, 0, MainWindow.width(), MainWindow.height() - 20))
        self.scrollArea_vault.setStyleSheet("")
        self.scrollArea_vault.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_vault.setWidgetResizable(True)
        self.scrollArea_vault.setObjectName("scrollArea_vault")
        self.scrollAreaWidgetContents_vault = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_vault.setGeometry(
            QtCore.QRect(0, 0, 436, 530))
        self.scrollAreaWidgetContents_vault.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_vault.setAutoFillBackground(False)
        self.scrollAreaWidgetContents_vault.setStyleSheet(
            "background-color: #34363a")
        self.scrollAreaWidgetContents_vault.setObjectName(
            "scrollAreaWidgetContents_vault")
        self.verticalLayout_vault = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_vault)
        self.verticalLayout_vault.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_vault.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_vault.setSpacing(0)
        self.verticalLayout_vault.setObjectName("verticalLayout_vault")
        self.groupBox_logoBackground_vault = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents_vault)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_logoBackground_vault.sizePolicy().hasHeightForWidth())
        self.groupBox_logoBackground_vault.setSizePolicy(sizePolicy)
        self.groupBox_logoBackground_vault.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_logoBackground_vault.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.groupBox_logoBackground_vault.setStyleSheet(
            "background-color: #454547;")
        self.groupBox_logoBackground_vault.setTitle("")
        self.groupBox_logoBackground_vault.setObjectName("groupBox")
        self.label_audit = QtWidgets.QLabel(self.groupBox_logoBackground_vault)
        self.label_audit.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - 500) / 2), round((self.groupBox_logoBackground_vault.height() - 150)/2), 500, 150))
        self.label_audit.setStyleSheet("")
        self.label_audit.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_audit.setScaledContents(True)
        self.label_audit.setObjectName("label_audit")
        self.verticalLayout_vault.addWidget(self.groupBox_logoBackground_vault)

        self.layoutWidget_vault = QtWidgets.QWidget(
            self.scrollAreaWidgetContents_vault)
        sizePolicy.setHeightForWidth(
            self.layoutWidget_vault.sizePolicy().hasHeightForWidth())
        self.layoutWidget_vault.setSizePolicy(sizePolicy)
        self.layoutWidget_vault.setMinimumSize(QtCore.QSize(0, 100))
        self.layoutWidget_vault.setStyleSheet("background-color: #d2c15d;")
        self.layoutWidget_vault.setObjectName("layoutWidget_vault")
        self.layoutWidget_vault.setProperty("class", "navBar_genPas")

        self.HomeBtn_vault = QtWidgets.QPushButton(self.layoutWidget_vault)
        self.HomeBtn_vault.setSizePolicy(sizePolicy)
        self.HomeBtn_vault.setStyleSheet("")
        self.HomeBtn_vault.setObjectName("HomeBtn_vault")
        self.HomeBtn_vault.setProperty("class", "navBar_btn")
        self.HomeBtn_vault.clicked.connect(self.homePg)
        self.SettingsBtn_vault = QtWidgets.QPushButton(self.layoutWidget_vault)

        self.SettingsBtn_vault.setSizePolicy(sizePolicy)
        self.SettingsBtn_vault.setStyleSheet("")
        self.SettingsBtn_vault.setObjectName("SettingsBtn_vault")
        self.SettingsBtn_vault.setProperty("class", "navBar_btn")
        self.AboutUsBtn_vault = QtWidgets.QPushButton(self.layoutWidget_vault)

        self.AboutUsBtn_vault.setSizePolicy(sizePolicy)
        self.AboutUsBtn_vault.setStyleSheet("")
        self.AboutUsBtn_vault.setObjectName("AboutUsBtn_vault")
        self.AboutUsBtn_vault.setProperty("class", "navBar_btn")
        self.dummyLabel_1_vault = QtWidgets.QLabel(self.layoutWidget_vault)
        self.dummyLabel_1_vault.setProperty("class", "QLabel_genPas")
        self.dummyLabel_2_vault = QtWidgets.QLabel(self.layoutWidget_vault)
        self.dummyLabel_2_vault.setProperty("class", "QLabel_genPas")

        self.navBar_vault = QtWidgets.QHBoxLayout(self.layoutWidget_vault)
        self.navBar_vault.setContentsMargins(10, 0, 0, 0)
        self.navBar_vault.setSpacing(0)
        self.navBar_vault.addWidget(self.HomeBtn_vault)
        self.navBar_vault.addWidget(self.SettingsBtn_vault)
        self.navBar_vault.addWidget(self.AboutUsBtn_vault)
        self.navBar_vault.addWidget(self.dummyLabel_1_vault)
        self.navBar_vault.addWidget(self.dummyLabel_2_vault)

        self.verticalLayout_vault.addWidget(self.layoutWidget_vault)

        self.groupBox_searchbar_vault = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents_vault)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_searchbar_vault.sizePolicy().hasHeightForWidth())
        self.groupBox_searchbar_vault.setSizePolicy(sizePolicy)
        self.groupBox_searchbar_vault.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox_searchbar_vault.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_searchbar_vault.setStyleSheet("""border-style: none;""")
        self.groupBox_searchbar_vault.setContentsMargins(10, 0, 10, 0)
        self.searchbar = QtWidgets.QLineEdit(self.groupBox_searchbar_vault)
        self.searchbar.setGeometry(QtCore.QRect(
            0, 0, MainWindow.width() - 28, 70))
        self.searchbar.textChanged.connect(self.update_display)
        self.searchbar.setPlaceholderText("Search the vault")
        self.searchbar.setContentsMargins(10, 10, 10, 10)
        self.searchbar.setStyleSheet(""" background-color: rgba(255, 255, 255, 50); font-size: 30px;
        border-style: none; padding-left: 10px;
        """)
        sizePolicy.setHeightForWidth(
            self.searchbar.sizePolicy().hasHeightForWidth())

        spacer_vault = QtWidgets.QSpacerItem(
            1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_vault.addWidget(self.groupBox_searchbar_vault)

        # list of names, widgets are stored in a dictionary
        widget_names = [
            "Facebook", "Twitter", "Instagram", "Telegram", "Snapchat"
        ]

        parameters = [
            {"website": "Snapchat", "username": "user01", "password": "12345"},
            {"website": "Twitter", "username": "user02", "password": "2345"},
            {"website": "Instagram", "username": "user03", "password": "45678"},
            {"website": "Facebook", "username": "user04", "password": "9alsdjf1"},
            {"website": "Steam", "username": "user05", "password": "L8nL77s"}
        ]

        self.widgets = []

        # Iterate the names, creating a new OnOffWidget for
        # each one, adding it to the layout and
        # storing a reference in the 'self.widgets' dict
        for x in parameters:
            website = x["website"]
            username = x["username"]
            password = x["password"]
            item = OnOffWidget(website, username, password)
            item.viewDetails(self.viewAccountPwd)
            item.setContentsMargins(0, 10, 0, 20)
            self.verticalLayout_vault.addWidget(item)
            self.widgets.append(item)

         # to maintain the positions of each items inside the layout
        self.verticalLayout_vault.addItem(spacer_vault)

        self.completer_vault = QtWidgets.QCompleter(widget_names)
        self.completer_vault.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer_vault)

        self.scrollArea_vault.setWidget(self.scrollAreaWidgetContents_vault)

        self.stackedWidget.addWidget(self.page_vault)
###############################################################################################
        self.page_audit = QtWidgets.QWidget()
        self.page_audit.setObjectName("page_audit")

        self.logoBackground_audit = QtWidgets.QLabel(self.page_audit)
        self.logoBackground_audit.setGeometry(
            QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
        self.logoBackground_audit.setProperty("class", "logoBackground_genPas")
        self.label_audit = QtWidgets.QLabel(self.page_audit)
        self.label_audit.setGeometry(QtCore.QRect(
            round((self.stackedWidget.width() - 560) / 2), 30, 560, 150))
        self.label_audit.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_audit.setScaledContents(True)
        self.label_audit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_audit.setObjectName("label_audit")
        self.label_audit.setProperty("class", "label_logo")

        self.layoutWidget_1_audit = QtWidgets.QWidget(self.page_audit)
        self.layoutWidget_1_audit.setGeometry(QtCore.QRect(
            0, self.logoBackground_audit.height() - 30, self.stackedWidget.width(), 100))
        self.layoutWidget_1_audit.setProperty("class", "navBar_genPas")

        self.HomeBtn_audit = QtWidgets.QPushButton(self.layoutWidget_1_audit)
        self.HomeBtn_audit.setProperty("class", "navBar_btn")
        self.HomeBtn_audit.clicked.connect(self.homePg)
        self.VaultBtn_audit = QtWidgets.QPushButton(self.layoutWidget_1_audit)
        self.VaultBtn_audit.setProperty("class", "navBar_btn")
        self.VaultBtn_audit.clicked.connect(self.vaultPg)
        self.SettingsBtn_audit = QtWidgets.QPushButton(
            self.layoutWidget_1_audit)
        self.SettingsBtn_audit.setProperty("class", "navBar_btn")
        self.AboutUsBtn_audit = QtWidgets.QPushButton(
            self.layoutWidget_1_audit)
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
        self.label_genPwd_Home.setText(_translate(
            "MainWindow", "1. Generate Passphrase"))
        self.label_genPwdDescription_Home.setText(_translate(
            "MainWindow", "Obtain a password using our simple but secure algorithm "))
        self.label_vault_Home.setText(
            _translate("MainWindow", "2. Access my vault"))
        self.label_vaultDescription_Home.setText(_translate(
            "MainWindow", "View & add passwords into your vault"))
        self.label_audit_Home.setText(
            _translate("MainWindow", "3. Security Audit"))
        self.label_auditDescription_Home.setText(_translate(
            "MainWindow", "Assess the security of the passwords in your vault"))
        self.label_14_Home.setText(_translate(
            "MainWindow", "Welcome, what would you like to do?"))
        self.settings_Home.setText(_translate("MainWindow", "Settings"))
        self.aboutUs_Home.setText(_translate("MainWindow", "About Us"))

        self.chromeButton_genPas.setText(
            _translate("MainWindow", "Google Chrome"))
        self.FireFoxButton_genPas.setText(_translate("MainWindow", "FireFox"))
        self.MicrosoftEdgeButton_genPas.setText(
            _translate("MainWindow", "Microsoft Edge"))
        self.OperaButton_genPas.setText(_translate("MainWindow", "Opera"))
        self.HomeBtn_genPas.setText(_translate("MainWindow", "Home"))
        self.VaultBtn_genPas.setText(_translate("MainWindow", "Vault"))
        self.SettingsBtn_genPas.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_genPas.setText(_translate("MainWindow", "About Us"))
        self.label_selectBrowser.setText(
            _translate("MainWindow", "1. Select browser"))
        self.genPwd_genPas.setText(_translate(
            "MainWindow", "Generate Password"))
        self.comboBox_Number_2_genPas.setItemText(
            0, _translate("MainWindow", "Number of words"))
        self.comboBox_Number_2_genPas.setItemText(
            1, _translate("MainWindow", "1"))
        self.comboBox_Number_2_genPas.setItemText(
            2, _translate("MainWindow", "2"))
        self.comboBox_Number_2_genPas.setItemText(
            3, _translate("MainWindow", "3"))
        self.comboBox_Number_2_genPas.setItemText(
            4, _translate("MainWindow", "4"))
        self.comboBox_Number_2_genPas.setItemText(
            5, _translate("MainWindow", "5"))
        self.comboBox_Number_3_genPas.setItemText(
            0, _translate("MainWindow", "Preference(s)"))
        self.dummyLabel_1_genPas.setText(_translate("MainWindow", ""))
        self.label_selectPreference_genPas.setText(_translate(
            "MainWindow", "2. Select number of words & Preferences"))
        self.dummyLabel_2_genPas.setText(_translate("MainWindow", ""))
        self.dummyLabel_3_genPas.setText(_translate("MainWindow", ""))
        self.dummyLabel_4_genPas.setText(_translate("MainWindow", ""))
        self.label_Title_genPas.setText(
            _translate("MainWindow", "Generate Passphrase"))
        self.label_genPas.setText(_translate("MainWindow", ""))

        self.label_audit.setText(_translate("MainWindow", ""))
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

    def update_display(self, text):

        for widget in self.widgets:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()

    def viewAccountPwd(self, pwd, username, account):
        self.page_dynamic = QtWidgets.QWidget()
        self.logoBackground_dynamic = QtWidgets.QLabel(self.page_dynamic)
        self.logoBackground_dynamic.setGeometry(
            QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
        self.logoBackground_dynamic.setProperty(
            "class", "logoBackground_genPas")
        self.label_dynamic = QtWidgets.QLabel(self.page_dynamic)
        self.label_dynamic.setGeometry(QtCore.QRect(
            round((self.stackedWidget.width() - 560) / 2), 30, 560, 150))
        self.label_dynamic.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_dynamic.setScaledContents(True)
        self.label_dynamic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dynamic.setObjectName("label_dynamic")
        self.label_dynamic.setProperty("class", "label_logo")

        self.layoutWidget_1_dynamic = QtWidgets.QWidget(self.page_dynamic)
        self.layoutWidget_1_dynamic.setGeometry(QtCore.QRect(
            0, self.logoBackground_dynamic.height() - 30, self.stackedWidget.width(), 100))
        self.layoutWidget_1_dynamic.setProperty("class", "navBar_genPas")

        self.HomeBtn_dynamic = QtWidgets.QPushButton(
            self.layoutWidget_1_dynamic)
        self.HomeBtn_dynamic.setProperty("class", "navBar_btn")
        self.HomeBtn_dynamic.setText("Home")
        self.HomeBtn_dynamic.clicked.connect(self.homePg)
        self.VaultBtn_dynamic = QtWidgets.QPushButton(
            self.layoutWidget_1_dynamic)
        self.VaultBtn_dynamic.setProperty("class", "navBar_btn")
        self.VaultBtn_dynamic.setText("Vault")
        self.VaultBtn_dynamic.clicked.connect(self.vaultPg)
        self.SettingsBtn_dynamic = QtWidgets.QPushButton(
            self.layoutWidget_1_dynamic)
        self.SettingsBtn_dynamic.setProperty("class", "navBar_btn")
        self.SettingsBtn_dynamic.setText("Settings")
        self.AboutUsBtn_dynamic = QtWidgets.QPushButton(
            self.layoutWidget_1_dynamic)
        self.AboutUsBtn_dynamic.setProperty("class", "navBar_btn")
        self.AboutUsBtn_dynamic.setText("About Us")
        self.dummyLabel_3_dynamic = QtWidgets.QLabel(
            self.layoutWidget_1_dynamic)
        self.dummyLabel_3_dynamic.setProperty("class", "QLabel_genPas")
        self.dummyLabel_4_dynamic = QtWidgets.QLabel(
            self.layoutWidget_1_dynamic)
        self.dummyLabel_4_dynamic.setProperty("class", "QLabel_genPas")

        self.navBar_audit = QtWidgets.QHBoxLayout(self.layoutWidget_1_dynamic)
        self.navBar_audit.addWidget(self.HomeBtn_dynamic)
        self.navBar_audit.addWidget(self.VaultBtn_dynamic)
        self.navBar_audit.addWidget(self.SettingsBtn_dynamic)
        self.navBar_audit.addWidget(self.AboutUsBtn_dynamic)
        self.navBar_audit.addWidget(self.dummyLabel_3_dynamic)
        self.navBar_audit.addWidget(self.dummyLabel_4_dynamic)

        self.groupBox_dynamic = QtWidgets.QGroupBox(self.page_dynamic)
        self.groupBox_dynamic.setGeometry(QtCore.QRect(round
                                                       ((self.stackedWidget.width(
                                                       ) - 1300) / 2), self.layoutWidget_1_dynamic.y()
                                                       + self.layoutWidget_1_dynamic.height() + 20, 1300, 500))
        self.groupBox_dynamic.setStyleSheet(""" border: 3px solid white; border-radius: 20px""")
        self.gridLayout_dynamic = QtWidgets.QGridLayout(self.groupBox_dynamic)
        self.gridLayout_dynamic.setContentsMargins(50, 25, 50, 100)
        self.gridLayout_dynamic.setHorizontalSpacing(50)
        self.gridLayout_dynamic.setVerticalSpacing(0)

        self.accountLabel_dynamic = QtWidgets.QLabel()
        self.accountLabel_dynamic.setText(account)
        self.accountLabel_dynamic.setStyleSheet("border-style: none;")
        self.accountLabel_dynamic.setProperty("class", "labels_dynamic")
        self.accountLabel_dynamic.setMaximumSize(QtCore.QSize(16777215, 50))
        self.userNameLabel_dynamic = QtWidgets.QLabel()
        self.userNameLabel_dynamic.setStyleSheet("border-style: none;")
        self.userNameLabel_dynamic.setProperty("class", "labels_dynamic")
        self.userNameLabel_dynamic.setText("User name:")
        self.pwdLabel_dynamic = QtWidgets.QLabel()
        self.pwdLabel_dynamic.setStyleSheet("border-style: none;")
        self.pwdLabel_dynamic.setProperty("class", "labels_dynamic")
        self.pwdLabel_dynamic.setText("Password / Passphrase:")

        self.userNameLE_dynamic = QtWidgets.QLineEdit(username.text())
        self.userNameLE_dynamic.setMaximumWidth(400)
        self.userNameLE_dynamic.setDisabled(True)
        self.userNameLE_dynamic.setStyleSheet("border-style: none;");
        self.userNameLE_dynamic.setProperty("class", "LE_dynamic")
        self.pwdLE_dynamic = QtWidgets.QLineEdit(pwd)
        self.pwdLE_dynamic.setMaximumWidth(400)
        self.pwdLE_dynamic.setStyleSheet("border-style: none;")
        self.pwdLE_dynamic.setProperty("class", "LE_dynamic")
        self.pwdLE_dynamic.setDisabled(True)
        self.copyBtn_dynamic = QtWidgets.QPushButton()
        self.copyBtn_dynamic.setText("Copy")
        self.copyBtn_dynamic.setMaximumWidth(200)
        self.copyBtn_dynamic.setStyleSheet("""
        QPushButton {
            font-size: 30px;
        }

        QPushButton:hover {
            border: 5px solid #6da4fc;
        }

        QPushButton:pressed {
            background-color: #6da4fc;
        }
        
        """)
        self.copyBtn_dynamic.setObjectName("copyButton_dynmaic")
        self.copyBtn_dynamic.clicked.connect(lambda: self.copyText(self.pwdLE_dynamic.text()))
        self.delBtn_dynamic = QtWidgets.QPushButton("Delete", self.groupBox_dynamic)
        self.styleSheet = """  
        QPushButton {
            font-size: 30px;
            background-color: #34363a;
            color: #ffffff;
            border-style: none;
        }

        QPushButton:hover {
            color: #d2c15d;
        }

        QPushButton:disabled {
            color: grey;
        }
        
        """
        self.delBtn_dynamic.setStyleSheet(self.styleSheet)
        self.delBtn_dynamic.setGeometry(QtCore.QRect(self.groupBox_dynamic.width() - 200, self.groupBox_dynamic.height() - 80, 180, 60))
        self.delBtn_dynamic.clicked.connect(self.deleteAcc)
        self.editBtn_dynamic = QtWidgets.QPushButton("Edit", self.groupBox_dynamic)
        self.editBtn_dynamic.setStyleSheet(self.styleSheet)
        self.editBtn_dynamic.setGeometry(QtCore.QRect(self.groupBox_dynamic.width() - 420, self.groupBox_dynamic.height() - 80, 180, 60))
        self.editBtn_dynamic.clicked.connect(self.editInfo)
        self.saveBtn_dynamic = QtWidgets.QPushButton("Save", self.groupBox_dynamic)
        self.saveBtn_dynamic.setStyleSheet(self.styleSheet)
        self.saveBtn_dynamic.setGeometry(QtCore.QRect(self.groupBox_dynamic.width() - 640, self.groupBox_dynamic.height() - 80, 180, 60))
        self.saveBtn_dynamic.setDisabled(True)
        self.saveBtn_dynamic.clicked.connect(self.saveInfo)
        self.gridLayout_dynamic.addWidget(self.accountLabel_dynamic, 0, 0, 1, 1)
        self.gridLayout_dynamic.addWidget(self.userNameLabel_dynamic, 1, 0, 1, 1)
        self.gridLayout_dynamic.addWidget(self.userNameLE_dynamic, 1, 1, 1, 1)
        self.gridLayout_dynamic.addWidget(self.pwdLabel_dynamic, 2, 0, 1, 1)
        self.gridLayout_dynamic.addWidget(self.pwdLE_dynamic, 2, 1, 1, 1)
        self.gridLayout_dynamic.addWidget(self.copyBtn_dynamic, 2, 2, 1, 1)
        
        self.qclip = QtWidgets.QApplication.clipboard()
        self.stackedWidget.addWidget(self.page_dynamic)
        self.stackedWidget.setCurrentWidget(self.page_dynamic)

    @QtCore.pyqtSlot()
    def copyText(self, pwd):
        self.qclip.setText(pwd)

    def editInfo(self):
        self.copyBtn_dynamic.setDisabled(True)
        self.pwdLE_dynamic.setDisabled(False)
        self.userNameLE_dynamic.setDisabled(False)
        self.pwdLE_dynamic.setStyleSheet("""background-color: white; color: black;""")
        self.userNameLE_dynamic.setStyleSheet("""background-color: white; color: black;""")
        self.editBtn_dynamic.setDisabled(True)
        self.saveBtn_dynamic.setDisabled(False)

    def saveInfo(self):
        self.copyBtn_dynamic.setDisabled(False)
        self.pwdLE_dynamic.setDisabled(True)
        self.userNameLE_dynamic.setDisabled(True)
        self.pwdLE_dynamic.setStyleSheet("""background-color: #34363a; color:white; border-style: none;""")
        self.userNameLE_dynamic.setStyleSheet("""background-color: #34363a; color:white; border-style: none;""")
        self.editBtn_dynamic.setDisabled(False)
        self.saveBtn_dynamic.setDisabled(True)

    def deleteAcc(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def showButton(self, btn):
        return btn.text()

    def appendToBtnList(self):
        sender_button = MainWindow.sender()

        #provide a check to see if the browser is already
        #selected
        if sender_button.text() not in self.btnList:
            self.btnList.append(sender_button.text())

        else:
            self.btnList.remove(sender_button.text())

    def appendToCBList_wordNo(self):

            selectedNumber  = self.comboBox_Number_2_genPas.currentText()

            if (len(selectedNumber) == 1):
                self.comboBox_wordNo = selectedNumber


    def genPassword(self):

        self.preferencesList = ['x', 'y', 'z', 'w', '1', '2','#','%']

        if (len(self.btnList) == 0 or self.comboBox_wordNo == "" ):
            print("Please try again.")
        else:     
            print(self.btnList)     
            print(self.comboBox_wordNo)
            generate_password(self.btnList, int(self.comboBox_wordNo), self.preferencesList)
               

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

        .QPushButton_genPas:checked{
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
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
            image: url(images/icons8-sort-down-100.png);
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
        
        .navBar_genPas {
            background-color: #d2c15d;
        }

        QGroupBox {
            border-style: none;
        }

        .labels_dynamic {
            border-style: none;
            font-size: 28px;
            color: #ffffff;
        }

        .LE_dynamic {
            border-style: none;
            background-color: #34363a;
            font-size: 40px;
            color: #ffffff;
        }
        

    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())