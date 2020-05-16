# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from customWidget import customGroupBox
from dialogBox import Ui_Dialog
from generator import Generator
from customCB import customComboBox
from customCB_symbol import customComboBox_symbol
from createNewAccount import createAccountForm
from setupPassword import setupPasForm
from enterVaultPass import vaultPassword

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 930)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/lock_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.qclip = QtWidgets.QApplication.clipboard()
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
            MainWindow.width() - 370, 575, 160, 35))
        self.settings_Home.setStyleSheet(
            "color: #34363a; background-color: #d2c15d; font-size: 20px")
        self.aboutUs_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.aboutUs_Home.setGeometry(QtCore.QRect(
            MainWindow.width() - 210, 575, 160, 35))
        self.aboutUs_Home.setStyleSheet(
            "color: #34363a; background-color: #d2c15d; font-size: 20px")

        self.label_14_Home = QtWidgets.QLabel(self.page_Home)
        self.label_14_Home.setGeometry(QtCore.QRect(
            0, self.logoBackground_Home.y() + 215, MainWindow.width(), 55))
        self.label_14_Home.setStyleSheet("font-size: 30px")
        self.label_14_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14_Home.setObjectName("label_14_Home")

        self.stackedWidget.addWidget(self.page_Home)
#################################################### Generator page #############################################################
        self.page_genPas = QtWidgets.QWidget()
        self.page_genPas.setObjectName("page_genPas")

        self.scrollArea_genPas = QtWidgets.QScrollArea(self.page_genPas)
        self.scrollArea_genPas.setGeometry(QtCore.QRect(
            0, 0, MainWindow.width(), MainWindow.height() - 20))
        self.scrollArea_genPas.setStyleSheet("")
        self.scrollArea_genPas.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_genPas.setWidgetResizable(True)
        self.scrollArea_genPas.setObjectName("scrollArea_genPas")
        self.scrollAreaWidgetContents_genPas = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_genPas.setGeometry(
            QtCore.QRect(0, 0, 436, 530))
        self.scrollAreaWidgetContents_genPas.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_genPas.setAutoFillBackground(False)
        self.scrollAreaWidgetContents_genPas.setStyleSheet(
            "background-color: #34363a")
        self.scrollAreaWidgetContents_genPas.setObjectName(
            "scrollAreaWidgetContents_genPas")
        self.verticalLayout_genPas = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_genPas)
        self.verticalLayout_genPas.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_genPas.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_genPas.setSpacing(0)
        self.verticalLayout_genPas.setObjectName("verticalLayout_genPas")
        self.groupBox_logoBackground_genPas = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents_genPas)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_logoBackground_genPas.sizePolicy().hasHeightForWidth())
        self.groupBox_logoBackground_genPas.setSizePolicy(sizePolicy)
        self.groupBox_logoBackground_genPas.setMinimumSize(
            QtCore.QSize(0, 250))
        self.groupBox_logoBackground_genPas.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.groupBox_logoBackground_genPas.setStyleSheet(
            "background-color: #454547;")
        self.groupBox_logoBackground_genPas.setTitle("")
        self.groupBox_logoBackground_genPas.setObjectName("groupBox")
        self.label_genPas = QtWidgets.QLabel(
            self.groupBox_logoBackground_genPas)
        self.label_genPas.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - 500) / 2), round((self.groupBox_logoBackground_genPas.height() - 150)/2), 500, 150))
        self.label_genPas.setStyleSheet("")
        self.label_genPas.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_genPas.setScaledContents(True)
        self.label_genPas.setObjectName("label_genPas")
        self.verticalLayout_genPas.addWidget(
            self.groupBox_logoBackground_genPas)

        self.layoutWidget_genPas = QtWidgets.QWidget(
            self.scrollAreaWidgetContents_genPas)
        sizePolicy.setHeightForWidth(
            self.layoutWidget_genPas.sizePolicy().hasHeightForWidth())
        self.layoutWidget_genPas.setSizePolicy(sizePolicy)
        self.layoutWidget_genPas.setMinimumSize(QtCore.QSize(0, 100))
        self.layoutWidget_genPas.setStyleSheet("background-color: #d2c15d;")
        self.layoutWidget_genPas.setObjectName("layoutWidget_genPas")
        self.layoutWidget_genPas.setProperty("class", "navBar_genPas")

        self.HomeBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_genPas)
        self.HomeBtn_genPas.setSizePolicy(sizePolicy)
        self.HomeBtn_genPas.setStyleSheet("")
        self.HomeBtn_genPas.setObjectName("HomeBtn_genPas")
        self.HomeBtn_genPas.setProperty("class", "navBar_btn")
        self.HomeBtn_genPas.clicked.connect(self.homePg)

        self.VaultBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_genPas)
        self.VaultBtn_genPas.setSizePolicy(sizePolicy)
        self.VaultBtn_genPas.setStyleSheet("")
        self.VaultBtn_genPas.setObjectName("HomeBtn_genPas")
        self.VaultBtn_genPas.setProperty("class", "navBar_btn")
        self.VaultBtn_genPas.clicked.connect(self.vaultPg)

        self.SettingsBtn_genPas = QtWidgets.QPushButton(
            self.layoutWidget_genPas)
        self.SettingsBtn_genPas.setSizePolicy(sizePolicy)
        self.SettingsBtn_genPas.setStyleSheet("")
        self.SettingsBtn_genPas.setObjectName("SettingsBtn_genPas")
        self.SettingsBtn_genPas.setProperty("class", "navBar_btn")

        self.AboutUsBtn_genPas = QtWidgets.QPushButton(
            self.layoutWidget_genPas)
        self.AboutUsBtn_genPas.setSizePolicy(sizePolicy)
        self.AboutUsBtn_genPas.setStyleSheet("")
        self.AboutUsBtn_genPas.setObjectName("AboutUsBtn_genPas")
        self.AboutUsBtn_genPas.setProperty("class", "navBar_btn")
        self.dummyLabel_1_genPas = QtWidgets.QLabel(self.layoutWidget_genPas)
        self.dummyLabel_1_genPas.setProperty("class", "QLabel_genPas")
        self.dummyLabel_1_genPas.setStyleSheet("border-style: none;")
        self.dummyLabel_2_genPas = QtWidgets.QLabel(self.layoutWidget_genPas)
        self.dummyLabel_2_genPas.setProperty("class", "QLabel_genPas")
        self.dummyLabel_2_genPas.setStyleSheet("border-style: none;")

        self.navBar_vault = QtWidgets.QHBoxLayout(self.layoutWidget_genPas)
        self.navBar_vault.setContentsMargins(20, 0, 0, 0)
        self.navBar_vault.setSpacing(0)
        self.navBar_vault.addWidget(self.HomeBtn_genPas)
        self.navBar_vault.addWidget(self.VaultBtn_genPas)
        self.navBar_vault.addWidget(self.SettingsBtn_genPas)
        self.navBar_vault.addWidget(self.AboutUsBtn_genPas)
        self.navBar_vault.addWidget(self.dummyLabel_1_genPas)
        self.navBar_vault.addWidget(self.dummyLabel_2_genPas)

        self.verticalLayout_genPas.addWidget(self.layoutWidget_genPas)

        #############################

        self.groupBox_genPas = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents_genPas)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_genPas.sizePolicy().hasHeightForWidth())
        self.groupBox_genPas.setSizePolicy(sizePolicy)
        self.groupBox_genPas.setMinimumSize(QtCore.QSize(0, 470))
        self.groupBox_genPas.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.groupBox_genPas.setObjectName("groupBox_genPas")
        self.groupBox_genPas.setProperty("class", "QGroupBox_genPas")
        self.verticalLayout_1_genPas = QtWidgets.QVBoxLayout(
            self.groupBox_genPas)
        self.verticalLayout_1_genPas.setObjectName("verticalLayout_1_genPas")
        self.container_1_genPas = QtWidgets.QWidget()
        self.container_1_genPas.setProperty("class", "containers_genPas")
        self.container_1_genPas.setStyleSheet("""
            background-color: #d2c15d;
            padding-bottom: 20px;
            border-radius:50px;
            border:2px solid #34363a;
        """)
        self.gridLayout_genPas = QtWidgets.QGridLayout(self.container_1_genPas)
        self.gridLayout_genPas.setContentsMargins(25, 10, 15, 10)
        self.gridLayout_genPas.setHorizontalSpacing(30)
        self.gridLayout_genPas.setVerticalSpacing(10)
        self.gridLayout_genPas.setObjectName("gridLayout_genPas")
        self.label_Title_genPas = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_genPas)
        self.label_Title_genPas.setStyleSheet("""color:#d2c15d; 
        font-size: 40px; font-family: Trebuchet MS; margin-left: 20px;""")

        self.label_Title_genPas.setGeometry(QtCore.QRect(
            self.groupBox_genPas.x() + 20, self.groupBox_genPas.y() - 70, 300, 70))

        self.verticalLayout_genPas.addWidget(self.label_Title_genPas)
        self.styleSheet = """
        QPushButton {
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
        QPushButton:hover {
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        QPushButtons:active {
            position:relative;
            top:1px;
        }

        QPushButton:checked{
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }

        QLabel {
            border-style: none;
            color:#34363a;
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
            image: url(images/icons8-sort-down-100.png);
            
        }

        QComboBox:disabled{
            background-color:#575a61;
            color:#fff6c2;
            font-size: 20px;
            padding-top: 5px;
            padding-bottom: 5px;
            padding-left: 10px;
        }

       

        """

        # buttons
        self.chromeButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon1_genPas = QtGui.QIcon()
        icon1_genPas.addPixmap(QtGui.QPixmap(
            "images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton_genPas.setIcon(icon1_genPas)
        self.chromeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton_genPas.setCheckable(True)
        self.chromeButton_genPas.setObjectName("chromeButton_genPas")
        self.chromeButton_genPas.setStyleSheet(self.styleSheet)
        self.FireFoxButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon2_genPas = QtGui.QIcon()
        icon2_genPas.addPixmap(QtGui.QPixmap(
            "images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton_genPas.setIcon(icon2_genPas)
        self.FireFoxButton_genPas.setCheckable(True)
        self.FireFoxButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton_genPas.setObjectName("FireFoxButton_genPas")
        self.FireFoxButton_genPas.setStyleSheet(self.styleSheet)
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
        self.MicrosoftEdgeButton_genPas.setStyleSheet(self.styleSheet)
        self.OperaButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon4_genPas = QtGui.QIcon()
        icon4_genPas.addPixmap(QtGui.QPixmap(
            "images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OperaButton_genPas.setIcon(icon4_genPas)
        self.OperaButton_genPas.setCheckable(True)
        self.OperaButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.OperaButton_genPas.setObjectName("OperaButton_genPas")
        self.OperaButton_genPas.setStyleSheet(self.styleSheet)

        self.FireFoxButton_genPas.clicked.connect(self.appendToBtnList)
        self.chromeButton_genPas.clicked.connect(self.appendToBtnList)
        self.MicrosoftEdgeButton_genPas.clicked.connect(self.appendToBtnList)
        self.OperaButton_genPas.clicked.connect(self.appendToBtnList)

        # btn array to store buttons that are selected
        self.btnList = []

        self.label_selectBrowser = QtWidgets.QLabel(self.groupBox_genPas)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectBrowser.setFont(font)
        self.label_selectBrowser.setAutoFillBackground(False)
        self.label_selectBrowser.setObjectName("label_selectBrowser")
        self.label_selectBrowser.setStyleSheet(self.styleSheet)

        self.gridLayout_genPas.addWidget(self.chromeButton_genPas, 1, 0, 1, 1)
        self.gridLayout_genPas.addWidget(self.FireFoxButton_genPas, 1, 1, 1, 1)
        self.gridLayout_genPas.addWidget(
            self.MicrosoftEdgeButton_genPas, 1, 3, 1, 1)
        self.gridLayout_genPas.addWidget(self.OperaButton_genPas, 1, 2, 1, 1)
        self.gridLayout_genPas.addWidget(self.label_selectBrowser, 0, 0, 1, 2)
        self.verticalLayout_1_genPas.addWidget(self.container_1_genPas)

        self.container_2_genPas = QtWidgets.QWidget()
        self.container_2_genPas.setSizePolicy(sizePolicy)
        self.container_2_genPas.setFixedHeight(280)
        self.container_2_genPas.setContentsMargins(0, 0, 0, 0)
        self.container_2_genPas.setProperty("class", "containers_genPas")
        self.container_2_genPas.setStyleSheet("""
            background-color: #d2c15d;
            padding-bottom: 20px;
            border-radius:50px;
            border:2px solid #34363a;
        """)

        self.label_selectPreference_genPas = QtWidgets.QLabel(
            self.container_2_genPas)
        self.label_selectPreference_genPas.setGeometry(
            QtCore.QRect(23, 10, 400, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectPreference_genPas.setText("Select number of words")
        self.label_selectPreference_genPas.setMinimumHeight(60)
        self.label_selectPreference_genPas.setFont(font)
        self.label_selectPreference_genPas.setAutoFillBackground(True)
        self.label_selectPreference_genPas.setObjectName(
            "label_selectPreference_genPas")
        self.label_selectPreference_genPas.setStyleSheet("""color: #34363a;
        border-style: none;
        """)

        self.comboBox_Number_2_genPas = QtWidgets.QComboBox(
            self.container_2_genPas)
        self.comboBox_Number_2_genPas.setGeometry(QtCore.QRect(
            round((self.scrollArea_genPas.width()-400)/2), 100, 400, 60))
        self.comboBox_Number_2_genPas.setMinimumHeight(50)
        self.comboBox_Number_2_genPas.setEnabled(False)
        self.comboBox_Number_2_genPas.setObjectName("comboBox_Number_2_genPas")
        self.comboBox_Number_2_genPas.setStyleSheet(self.styleSheet)
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.addItem("")
        self.comboBox_Number_2_genPas.currentIndexChanged.connect(
            self.showExtraCB)

        self.comboBox_Number_2_genPas.setStyleSheet("""
            background-color: #34363a;
            color: #d2c15d;
            border: 2px solid black;
            border-radius: 0px;
            padding:0px;
            padding-left: 10px;     
            font-size: 20px;  
        """)

        #number of word comboBox selected value
        self.comboBox_wordNo = 0

        self.resetComboBox_genPas = QtWidgets.QPushButton(
            self.container_2_genPas)
        self.resetComboBox_genPas.setText("Reset number of words")
        self.resetComboBox_genPas.setGeometry(QtCore.QRect(
            round((self.scrollArea_genPas.width()-300)/2), 200, 300, 50))
        self.resetComboBox_genPas.setEnabled(False)
        self.resetComboBox_genPas.setMaximumWidth(300)
        self.resetComboBox_genPas.setMinimumHeight(60)
        self.resetComboBox_genPas.clicked.connect(self.resetNumber)

        self.styleSheet = """ 
            QPushButton {
                border: none;
                color: #d2c15d;  
                background-color: #34363a;
                font-size: 23px;
                padding: 0px;
            }

            QPushButton:disabled {
                border: none;
                color: #fff6c2;  
                background-color: #575a61;
                font-size: 23px;
                padding: 0px;
            } 
        """
        self.resetComboBox_genPas.setStyleSheet(self.styleSheet)

        self.verticalLayout_1_genPas.addWidget(self.container_2_genPas)

        spacer_genPas = QtWidgets.QSpacerItem(
            1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

        self.verticalLayout_genPas.addWidget(self.groupBox_genPas)

        self.verticalLayout_genPas.addItem(spacer_genPas)

        self.scrollArea_genPas.setWidget(self.scrollAreaWidgetContents_genPas)

        self.stackedWidget.addWidget(self.page_genPas)
################################################## Vault  Page #########################################################
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

        self.styleSheet = """
            font-size: 30px;
            color: #d2c15d;
        """

##################################### VAULT RELEVANT DEFINITION ######################################
        self.welcomeSign = QtWidgets.QWidget()
        self.wcs_layout = QtWidgets.QHBoxLayout(self.welcomeSign)
        self.welcome = QtWidgets.QLabel("Welcome to the vault!")
        self.welcome.setStyleSheet(self.styleSheet)
        self.addNewAcc = QtWidgets.QPushButton("Add New Account")
        self.addNewAcc.setObjectName("addNewAcc")
        self.addNewAcc.setStyleSheet(self.styleSheet)
        self.addNewAcc.clicked.connect(self.createAcc)
        self.wcs_layout.addWidget(self.welcome)
        self.wcs_layout.addWidget(self.addNewAcc)
        self.verticalLayout_vault.addWidget(self.welcomeSign)

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
        self.widget_names = [
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

        # Iterate the names, creating a new customGroupBox for
        # each one, adding it to the layout and
        # storing a reference in the 'self.widgets' dict
        for x in parameters:
            website = x["website"]
            username = x["username"]
            password = x["password"]
            item = customGroupBox(website, username, password)
            item.viewDetails(self.viewAccountPwd)
            item.setContentsMargins(0, 10, 0, 20)
            self.verticalLayout_vault.addWidget(item)
            self.widgets.append(item)
            if website not in self.widget_names:
                self.widget_names.append(website)

         # to maintain the positions of each items inside the layout
        self.verticalLayout_vault.addItem(spacer_vault)

        self.completer_vault = QtWidgets.QCompleter(self.widget_names)
        self.completer_vault.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer_vault)

        self.scrollArea_vault.setWidget(self.scrollAreaWidgetContents_vault)

        self.stackedWidget.addWidget(self.page_vault)

############################################# Audit page ########################################################

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

        self.securityAuditWidget = QtWidgets.QWidget(self.page_audit)
        self.saWidgetLayout = QtWidgets.QVBoxLayout(self.securityAuditWidget)
        self.securityAuditWidget.setGeometry(QtCore.QRect(
            round((self.stackedWidget.width() - 570) / 2), 600, 500, 300))
        self.securityAuditWidget.setStyleSheet("""
            border: 2px dashed white;
        """)
        font.setPointSize(14)
        self.resultLabel = QtWidgets.QLabel(self.page_audit)
        self.resultLabel.setText("Your password strength:" )     
        self.resultLabel.setMaximumHeight(60)      
        self.resultLabel.setStyleSheet("""
        
            border: 0px solid white;
        
        """)
        self.passwordStrengthAuditLE = QtWidgets.QLineEdit(self.page_audit)
        self.passwordStrengthAuditLE.setMaximumHeight(60)
        self.passwordStrengthAuditLE.setFont(font)
        self.saWidgetLayout.addWidget(self.passwordStrengthAuditLE)
        self.saWidgetLayout.addWidget(self.resultLabel)
        
        self.imageLabel = QtWidgets.QLabel(self.page_audit)
        self.imageLabel.setPixmap(QtGui.QPixmap("images/security_Audit_adjust.jpg"))
        self.imageLabel.setGeometry(QtCore.QRect(
            round((self.stackedWidget.width() - 500) / 2), 400, 500, 200))


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
            _translate("MainWindow", "Select browser"))
        # self.genPwd_genPas.setText(_translate(
        #    "MainWindow", "Generate Password"))
        self.comboBox_Number_2_genPas.setItemText(
            0, _translate("MainWindow", "Number of words"))
        self.comboBox_Number_2_genPas.setItemText(
            1, _translate("MainWindow", "4"))
        self.comboBox_Number_2_genPas.setItemText(
            2, _translate("MainWindow", "5"))
        self.comboBox_Number_2_genPas.setItemText(
            3, _translate("MainWindow", "6"))
        self.comboBox_Number_2_genPas.setItemText(
            4, _translate("MainWindow", "7"))
        self.comboBox_Number_2_genPas.setItemText(
            5, _translate("MainWindow", "8"))
        # self.comboBox_Number_3_genPas.setItemText(
        #    0, _translate("MainWindow", "Preference(s)"))
        self.dummyLabel_1_genPas.setText(_translate("MainWindow", ""))
        # self.label_selectPreference_genPas.setText(_translate(
        #    "MainWindow", "2. Select number of words & Preferences"))
        self.dummyLabel_2_genPas.setText(_translate("MainWindow", ""))
        #self.dummyLabel_3_genPas.setText(_translate("MainWindow", ""))
        #self.dummyLabel_4_genPas.setText(_translate("MainWindow", ""))
        self.label_Title_genPas.setText(
            _translate("MainWindow", "Generate Passphrase"))

        self.label_audit.setText(_translate("MainWindow", ""))
        self.HomeBtn_vault.setText(_translate("MainWindow", "Home"))
        self.SettingsBtn_vault.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_vault.setText(_translate("MainWindow", "About Us"))

        self.HomeBtn_audit.setText(_translate("MainWindow", "Home"))
        self.VaultBtn_audit.setText(_translate("MainWindow", "Vault"))
        self.SettingsBtn_audit.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_audit.setText(_translate("MainWindow", "About Us"))

############################################### User define functions ##################################################################

    def homePg(self):
        self.stackedWidget.setCurrentIndex(0)

    def genPasPg(self):
        self.stackedWidget.setCurrentIndex(1)

    def vaultPg(self):
        # check if the passwords are identical while setting up  
        checkPassword = False    
        # check if user clicked cancel button on the setup window
        popWindow = True 
        # check if the passwords are identical while entering vault
        checkEnterPassword = False 
        # check if user clicked cancel button on the enter password
        # window
        popEnterPass = True

        #ezPass folder path
        folder_path = os.path.expanduser(r'~\Documents\ezPass\UserKey')

        #userkey.txt file path
        userkey_file = os.path.expanduser(r'~\Documents\ezPass\UserKey\userkey.txt')

        #if ezPass folder is not exist or userkey.txt is not exist
        if (not os.path.isdir(folder_path) or not os.path.isfile(userkey_file)):
            print("test")
            checkPassword = False
            if (not os.path.isdir(folder_path)):
                #create ezPass user password folder
                os.mkdir(folder_path)
               
               
            #change directory to folder path
            os.chdir(folder_path)    
            setupPassword = setupPasForm()
            
            # while the passwords entered are not the same and the user 
            # did not cancel the setup
            while (checkPassword != True and popWindow): 
                # if user clicked submit get both of the entered password
                if setupPassword.exec_():
                    password = setupPassword.password.text()
                    confirmPass = setupPassword.confirmPass.text()
                    #check if they are the same
                    if (password == confirmPass and password != ""):
                        #open a file to record the password
                        with open('userkey.txt', "w") as f:
                            f.write(password) 
                        f.close()
                        checkPassword = True

                    else:
                        Dialog = QtWidgets.QDialog()
                        ui = Ui_Dialog()
                        ui.setupUi(Dialog, "Please retry!")
                        Dialog.show()
                        Dialog.exec_()
                
                #user cancel the setup 
                else:
                    popWindow = False
                

            if (checkPassword):
                self.stackedWidget.setCurrentIndex(2)  

            

        else:
            
            #created a enter vault password window
            enterVault = vaultPassword()

            #change directory to folder path
            os.chdir(folder_path) 

            while ( checkEnterPassword == False and popEnterPass):
                createdPassword = ""
                if enterVault.exec_():
                    enteredPassword = enterVault.password.text()
                    #open userkey.txt to read the password
                    if(os.path.isfile(userkey_file)):
                        with open('userkey.txt', "r") as f:
                            createdPassword = f.read() 
                            print(createdPassword)
                        f.close()
                        if (createdPassword == enteredPassword):
                            checkEnterPassword = True

                        else:
                            Dialog = QtWidgets.QDialog()
                            ui = Ui_Dialog()
                            ui.setupUi(Dialog, "Incorrect Password!")
                            Dialog.show()
                            Dialog.exec_()

                else:
                    popEnterPass = False
        
            if(checkEnterPassword):
                self.stackedWidget.setCurrentIndex(2)
            
                  

            

    def auditPg(self):
        self.stackedWidget.setCurrentIndex(3)

    #if user input can be found inside the list
    #show the widget (groupbox)
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
        self.groupBox_dynamic.setStyleSheet(
            """ border: 3px solid white; border-radius: 20px""")
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
        self.userNameLE_dynamic.setStyleSheet("border-style: none;")
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
        self.copyBtn_dynamic.clicked.connect(
            lambda: self.copyText(self.pwdLE_dynamic.text()))
        self.delBtn_dynamic = QtWidgets.QPushButton(
            "Delete", self.groupBox_dynamic)
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
        self.delBtn_dynamic.setGeometry(QtCore.QRect(
            self.groupBox_dynamic.width() - 200, self.groupBox_dynamic.height() - 80, 180, 60))
        self.delBtn_dynamic.clicked.connect(lambda: self.deleteAcc(username, account))
        self.editBtn_dynamic = QtWidgets.QPushButton(
            "Edit", self.groupBox_dynamic)
        self.editBtn_dynamic.setStyleSheet(self.styleSheet)
        self.editBtn_dynamic.setGeometry(QtCore.QRect(
            self.groupBox_dynamic.width() - 420, self.groupBox_dynamic.height() - 80, 180, 60))
        self.editBtn_dynamic.clicked.connect(self.editInfo)
        self.saveBtn_dynamic = QtWidgets.QPushButton(
            "Save", self.groupBox_dynamic)
        self.saveBtn_dynamic.setStyleSheet(self.styleSheet)
        self.saveBtn_dynamic.setGeometry(QtCore.QRect(
            self.groupBox_dynamic.width() - 640, self.groupBox_dynamic.height() - 80, 180, 60))
        self.saveBtn_dynamic.setDisabled(True)
        self.saveBtn_dynamic.clicked.connect(self.saveInfo)
        self.gridLayout_dynamic.addWidget(
            self.accountLabel_dynamic, 0, 0, 1, 1)
        self.gridLayout_dynamic.addWidget(
            self.userNameLabel_dynamic, 1, 0, 1, 1)
        self.gridLayout_dynamic.addWidget(self.userNameLE_dynamic, 1, 1, 1, 1)
        self.gridLayout_dynamic.addWidget(self.pwdLabel_dynamic, 2, 0, 1, 1)
        self.gridLayout_dynamic.addWidget(self.pwdLE_dynamic, 2, 1, 1, 1)
        self.gridLayout_dynamic.addWidget(self.copyBtn_dynamic, 2, 2, 1, 1)

        
        self.stackedWidget.addWidget(self.page_dynamic)
        self.stackedWidget.setCurrentWidget(self.page_dynamic)

    @QtCore.pyqtSlot()
    def copyText(self, pwd):
        self.qclip.setText(pwd)

    def editInfo(self):
        self.copyBtn_dynamic.setDisabled(True)
        self.pwdLE_dynamic.setDisabled(False)
        self.userNameLE_dynamic.setDisabled(False)
        self.pwdLE_dynamic.setStyleSheet(
            """background-color: white; color: black;""")
        self.userNameLE_dynamic.setStyleSheet(
            """background-color: white; color: black;""")
        self.editBtn_dynamic.setDisabled(True)
        self.saveBtn_dynamic.setDisabled(False)

    def saveInfo(self):
        self.copyBtn_dynamic.setDisabled(False)
        self.pwdLE_dynamic.setDisabled(True)
        self.userNameLE_dynamic.setDisabled(True)
        self.pwdLE_dynamic.setStyleSheet(
            """background-color: #34363a; color:white; border-style: none;""")
        self.userNameLE_dynamic.setStyleSheet(
            """background-color: #34363a; color:white; border-style: none;""")
        self.editBtn_dynamic.setDisabled(False)
        self.saveBtn_dynamic.setDisabled(True)

    # a function that create Pop up windows when user deletes an
    # account from vault page, and remove the related groupbox 
    # from vault page
    def deleteAcc(self, username, account):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, "Confirm deletion of account?")
        Dialog.show()

        if Dialog.exec_():
            for i in self.widgets:
                if (i.uname == username.text() and i.name == account):
                    i.delete()
                    self.widgets.pop(self.widgets.index(i))
                    self.verticalLayout_vault.removeWidget(i)
            self.stackedWidget.setCurrentIndex(2)

        else:
            print("Cancel!")

            
    # useless function 
    def showButton(self, btn):
        return btn.text()

    # a button will be append to the button list (self.btnList) when it is clicked 
    def appendToBtnList(self):
        sender_button = MainWindow.sender()
        self.comboBox_Number_2_genPas.setEnabled(True) 
        # provide a check to see if the browser is already
        # selected
        if sender_button.text() not in self.btnList:
            self.btnList.append(sender_button.text())

        else:
            self.btnList.remove(sender_button.text())
            if (len(self.btnList) == 0):
                self.comboBox_Number_2_genPas.setDisabled(True)

    #show the preferences comboboxes including starting alphabets
    # and number/symbols at the bottom of genPas page
    def showExtraCB(self):

        self.MicrosoftEdgeButton_genPas.setDisabled(True)
        self.FireFoxButton_genPas.setDisabled(True)
        self.chromeButton_genPas.setDisabled(True)
        self.OperaButton_genPas.setDisabled(True)

        selectedNumber = self.comboBox_Number_2_genPas.currentText()

        # a list that stores the comboboxes of preferences 
        self.generalPreferenceList = []

        self.cb_dynamic = QtWidgets.QGroupBox()
        self.cb_dynamic_layoutWidget = QtWidgets.QWidget()
        self.cb_dynamic_Vlayout = QtWidgets.QVBoxLayout(self.cb_dynamic)
        self.preference_Label_genPas = QtWidgets.QLabel()
        self.preference_Label_genPas.setText("Select Preferred Alphabets")
        self.cb_2_dynamic = QtWidgets.QGroupBox()

        self.cb_dynamic_Vlayout.addWidget(self.preference_Label_genPas)
        self.cb_dynamic_Hlayout = QtWidgets.QHBoxLayout()
        self.cb_dynamic_2_Hlayout = QtWidgets.QHBoxLayout(self.cb_2_dynamic)

        self.cb_dynamic_symbol = QtWidgets.QGroupBox()
        self.cb_dynamic_symbol_layoutWidget = QtWidgets.QWidget()
        self.cb_dynamic_symbol_Vlayout = QtWidgets.QVBoxLayout(
            self.cb_dynamic_symbol)
        self.preference_Label_symbol_genPas = QtWidgets.QLabel()
        self.preference_Label_symbol_genPas.setText(
            "Select Preferred Symbols / Number")
        self.cb_2_dynamic_symbol = QtWidgets.QGroupBox()

        self.cb_dynamic_symbol_Vlayout.addWidget(
            self.preference_Label_symbol_genPas)
        self.cb_dynamic_symbol_Hlayout = QtWidgets.QHBoxLayout()
        self.cb_dynamic_2_symbol_Hlayout = QtWidgets.QHBoxLayout(
            self.cb_2_dynamic_symbol)

        self.genPasRowLayout_widget = QtWidgets.QWidget()
        self.genPasRowLayout_widget.setMinimumHeight(100)
        self.gpHLayout = QtWidgets.QHBoxLayout(self.genPasRowLayout_widget)

        self.styleSheet = """ 
            QPushButton {
                background-color: #d2c15d;
                font-size: 20px;
                border-radius: 20px;
            }

            QPushButton:disabled{
                background-color: #ffffb3;
            }
        
        """
        self.cancelPreferenceButton = QtWidgets.QPushButton("Reselect All")
        self.cancelPreferenceButton.setDisabled(True)
        self.cancelPreferenceButton.setStyleSheet(self.styleSheet)
        self.cancelPreferenceButton.setMinimumHeight(70)
        self.cancelPreferenceButton.setMaximumWidth(350)
        self.cancelPreferenceButton.clicked.connect(self.cancelPreference)
        self.confirmPreferenceButton = QtWidgets.QPushButton("Confirm Preferences")  
        self.confirmPreferenceButton.setStyleSheet(self.styleSheet)  
        self.confirmPreferenceButton.setMinimumHeight(70)
        self.confirmPreferenceButton.setMaximumWidth(350)
        self.confirmPreferenceButton.clicked.connect(self.confirm_selections)
        self.generatePasswordButton = QtWidgets.QPushButton("Generate Passphrase")
        self.generatePasswordButton.setStyleSheet(self.styleSheet)
        self.generatePasswordButton.setDisabled(True)
        self.generatePasswordButton.setMinimumHeight(70)
        self.generatePasswordButton.setMaximumWidth(350)
        self.generatePasswordButton.clicked.connect(self.genPassword)

        self.gpHLayout.addWidget(self.cancelPreferenceButton)
        self.gpHLayout.addWidget(self.confirmPreferenceButton)
        self.gpHLayout.addWidget(self.generatePasswordButton)


        #if number of words combo box
        if (len(selectedNumber) == 1):
            self.comboBox_Number_2_genPas.setEnabled(False)
            self.resetComboBox_genPas.setEnabled(True)
            self.comboBox_wordNo = int(selectedNumber)

            for i in range(int(self.comboBox_wordNo)):
                cbox = customComboBox()
                if i < 4:
                    self.cb_dynamic_Hlayout.addWidget(cbox)
                    
                else:
                    self.cb_dynamic_2_Hlayout.addWidget(cbox)
                #append all the comboBoxes that stores 
                #starting alphabets to a list
                self.generalPreferenceList.append(cbox)

            self.cb_dynamic_Vlayout.addLayout(self.cb_dynamic_Hlayout)
            self.verticalLayout_genPas.addWidget(self.cb_dynamic)

            if(int(self.comboBox_wordNo) > 4):
                if (self.comboBox_wordNo == 5):
                    spacer_dynamic = QtWidgets.QSpacerItem(
                        1036, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    self.cb_dynamic_2_Hlayout.addItem(spacer_dynamic)

                elif(self.comboBox_wordNo == 6):
                    spacer_dynamic = QtWidgets.QSpacerItem(
                        690, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    self.cb_dynamic_2_Hlayout.addItem(spacer_dynamic)

                elif(self.comboBox_wordNo == 7):
                    spacer_dynamic = QtWidgets.QSpacerItem(
                        345, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    self.cb_dynamic_2_Hlayout.addItem(spacer_dynamic)

                self.verticalLayout_genPas.addWidget(self.cb_2_dynamic)

            for i in range(self.comboBox_wordNo):
                cbox_symbol = customComboBox_symbol()
                if i < 4:
                    self.cb_dynamic_symbol_Hlayout.addWidget(cbox_symbol)
                else:
                    self.cb_dynamic_2_symbol_Hlayout.addWidget(cbox_symbol)


                self.generalPreferenceList.append(cbox_symbol)

            self.cb_dynamic_symbol_Vlayout.addLayout(
                self.cb_dynamic_symbol_Hlayout)
            self.verticalLayout_genPas.addWidget(self.cb_dynamic_symbol)

            if(self.comboBox_wordNo > 4):
                if (self.comboBox_wordNo == 5):
                    self.cb_dynamic_2_symbol_Hlayout.addItem(spacer_dynamic)

                elif(self.comboBox_wordNo == 6):
                    self.cb_dynamic_2_symbol_Hlayout.addItem(spacer_dynamic)

                elif(self.comboBox_wordNo == 7):
                    self.cb_dynamic_2_symbol_Hlayout.addItem(spacer_dynamic)

                self.verticalLayout_genPas.addWidget(self.cb_2_dynamic_symbol)
            
            self.verticalLayout_genPas.addWidget(self.genPasRowLayout_widget)

        else:
            pass

        
    def genPassword(self):

        self.styleSheet = """ 
            QPushButton {
                background-color: #d2c15d;
                font-size: 20px;
                border-radius: 20px;
                margin-left: 40px;
            }


        """
        self.generatePasswordButton.setDisabled(True)
        self.cancelPreferenceButton.setDisabled(True)
    
        self.resultLayoutWidget = QtWidgets.QWidget()
        self.resultLayoutWidget.setMinimumHeight(300)
        self.resultLayoutWidget.setStyleSheet("""
            margin-top: 50px;
            background-color: #ffffff;
        """)
        self.resultWidget_HLayout = QtWidgets.QHBoxLayout(self.resultLayoutWidget)
        self.finalResult = QtWidgets.QLabel()
        self.finalResult.setStyleSheet(self.styleSheet)
        self.finalResult.setMinimumHeight(60)
        self.resetAllbtn = QtWidgets.QPushButton("Reset all")
        self.resetAllbtn.setStyleSheet(self.styleSheet)
        self.resetAllbtn.clicked.connect(self.resetAll)
        self.resetAllbtn.setMinimumHeight(150)
        self.copyPassPhrasebtn = QtWidgets.QPushButton("Copy")
        self.copyPassPhrasebtn.setStyleSheet(self.styleSheet)
        self.copyPassPhrasebtn.setMinimumHeight(150)
        self.copyPassPhrasebtn.clicked.connect( lambda: self.copyText(self.finalResult.text()))
        self.displayText = QtWidgets.QLabel("Generated passphrase: ")

        if (len(self.btnList) == 0 or self.comboBox_wordNo == ""):
            print("Please try again.")
        else:
            generator = Generator()
            self.finalResult.setText(generator.generate_password(self.btnList, int(
                self.comboBox_wordNo), self.preferenceList))
            self.resultWidget_HLayout.addWidget(self.displayText)
            self.resultWidget_HLayout.addWidget(self.finalResult)
            self.resultWidget_HLayout.addWidget(self.copyPassPhrasebtn)
            self.resultWidget_HLayout.addWidget(self.resetAllbtn)
            

            self.verticalLayout_genPas.addWidget(self.resultLayoutWidget)
            

    def resetNumber(self):
        selectedNumber = self.comboBox_Number_2_genPas.currentText()

        self.comboBox_Number_2_genPas.setEnabled(True)
        self.resetComboBox_genPas.setEnabled(False)
        self.cb_dynamic.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.cb_dynamic)
        self.cb_dynamic_symbol.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.cb_dynamic_symbol)
        self.genPasRowLayout_widget.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.genPasRowLayout_widget)

        if (self.comboBox_wordNo > 4):
            self.cb_2_dynamic.setHidden(True) 
            self.cb_2_dynamic_symbol.setHidden(True)
            self.verticalLayout_genPas.removeWidget(self.cb_2_dynamic)
            self.verticalLayout_genPas.removeWidget(self.cb_2_dynamic_symbol)

    #set the buttons to be editable / clickable again 
    def cancelPreference(self):
        self.confirmPreferenceButton.setDisabled(False)
        self.cancelPreferenceButton.setDisabled(True)
        self.generatePasswordButton.setDisabled(True)
        self.resetComboBox_genPas.setDisabled(False)
        self.MicrosoftEdgeButton_genPas.setDisabled(False)
        self.FireFoxButton_genPas.setDisabled(False)
        self.OperaButton_genPas.setDisabled(False)

        self.cb_dynamic.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.cb_dynamic)
        self.cb_dynamic_symbol.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.cb_dynamic_symbol)
        self.verticalLayout_genPas.removeWidget(self.genPasRowLayout_widget)

        if (self.comboBox_wordNo > 4):
            self.cb_2_dynamic.setHidden(True) 
            self.cb_2_dynamic_symbol.setHidden(True)
            self.verticalLayout_genPas.removeWidget(self.cb_2_dynamic)
            self.verticalLayout_genPas.removeWidget(self.cb_2_dynamic_symbol)
       
        self.chromeButton_genPas.setDisabled(False)

        for i in self.generalPreferenceList:
            i.setDisabled(False)

    #set the buttons to be disabled and append the selected once to a list
    def confirm_selections(self):
        self.confirmPreferenceButton.setDisabled(True)
        self.comboBox_Number_2_genPas.setDisabled(True)
        self.cancelPreferenceButton.setDisabled(False)
        self.generatePasswordButton.setDisabled(False)
        self.resetComboBox_genPas.setDisabled(True)
        self.MicrosoftEdgeButton_genPas.setDisabled(True)
        self.FireFoxButton_genPas.setDisabled(True)
        self.OperaButton_genPas.setDisabled(True)
        self.chromeButton_genPas.setDisabled(True)
        self.preferenceList = []

        for i in self.generalPreferenceList:
            i.setDisabled(True)
            self.preferenceList.append(i.currentText())


    # this function will be used to enable the corresponding 
    # buttons & combo boxes to be editable again
    def resetAll(self):
        self.resetComboBox_genPas.setEnabled(False)
        self.cb_dynamic.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.cb_dynamic)
        self.cb_dynamic_symbol.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.cb_dynamic_symbol)
        self.genPasRowLayout_widget.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.genPasRowLayout_widget)
        self.resultLayoutWidget.setHidden(True)
        self.verticalLayout_genPas.removeWidget(self.resultLayoutWidget)
        self.MicrosoftEdgeButton_genPas.setDisabled(False)
        self.FireFoxButton_genPas.setDisabled(False)
        self.OperaButton_genPas.setDisabled(False)
        self.chromeButton_genPas.setDisabled(False)

        if (self.comboBox_wordNo > 4):
            self.cb_2_dynamic.setHidden(True)
            self.cb_2_dynamic_symbol.setHidden(True)
            self.verticalLayout_genPas.removeWidget(self.cb_2_dynamic)
            self.verticalLayout_genPas.removeWidget(self.cb_2_dynamic_symbol)

    def createAcc(self):
        login = createAccountForm()
        spacer_vault = QtWidgets.QSpacerItem(
            1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        if login.exec_():
            website = login.website.text()
            username = login.username.text()
            password = login.password.text()
            if ( website != "" and username != "" and password != ""):
                item = customGroupBox(website, username, password)
                item.viewDetails(self.viewAccountPwd)
                item.setContentsMargins(0, 10, 0, 20)
                self.verticalLayout_vault.addWidget(item)
                self.widgets.append(item)
                self.verticalLayout_vault.addItem(spacer_vault)
                if website not in self.widget_names:
                    self.widget_names.append(website)

            else: 
                Dialog = QtWidgets.QDialog()
                ui = Ui_Dialog()
                ui.setupUi(Dialog, "Information insufficient!")
                Dialog.show()
                Dialog.exec_()
                ##testing
      
    
        


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

        
        .QGroupBox_genPas {
            background-color:#34363a;
            border: none;
        }

        .QLabel_genPas {
            color:#34363a; 
            background-color:#d2c15d;
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
