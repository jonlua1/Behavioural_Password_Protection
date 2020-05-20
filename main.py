# -*- coding: utf-8 -*-

# Icons from generator page is from icons8.com!!!

import os
import shutil
import resource
import sys 


from PyQt5 import QtCore, QtGui, QtWidgets
from zxcvbn import zxcvbn

try:
    
    from PyQt5.QtWinExtras import QtWin
    myappid = 'SIM_student.FYP.EzPass.v1.0'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass

from frontend.customWidget import customGroupBox
from frontend.dialogBox import Ui_Dialog
from frontend.customCB import customComboBox
from frontend.customCB_symbol import customComboBox_symbol
from frontend.createNewAccount import createAccountForm
from frontend.setupPassword import setupPasForm
from frontend.aboutUs import Ui_AboutUs
from frontend.settings import Ui_Settings
from frontend.enterVaultPass import vaultPassword


#import from backend folder
from backend.password_generator import Password_Generator
from backend.vault import Vault
from backend.check_running_process import check_running_process


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 930)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/lock_icon.png"),
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

        self.logoPixmap = QtGui.QPixmap(":/images/images/ezPassLogo.PNG")
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
        self.label_genPwd_Home.setStyleSheet("font-size: 35px; font-weight: bold;")
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
            QtGui.QPixmap(":images/images/generate_password.jpg"))
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
        self.label_vault_Home.setStyleSheet("font-size: 30px; font-weight: bold;")
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
            QtGui.QPixmap(":images/images/smaller_vault.png"))
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
        self.label_audit_Home.setStyleSheet("font-size: 30px; font-weight: bold;")
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
            QtGui.QPixmap(":images/images/security_Audit_adjust.jpg"))
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
        self.label_Home.setPixmap(self.logoPixmap)
        self.label_Home.setScaledContents(True)
        self.label_Home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Home.setObjectName("label_Home")
        self.label_Home.setProperty("class", "label_logo")

        self.settings_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.settings_Home.setGeometry(QtCore.QRect(
            MainWindow.width() - 370, 575, 160, 35))
        self.settings_Home.setStyleSheet(
            "color: #34363a; background-color: #d2c15d; font-size: 20px; font-weight: bold;")
        self.settings_Home.clicked.connect(self.settingsPg)
        self.aboutUs_Home = QtWidgets.QPushButton(self.groupBox_Home)
        self.aboutUs_Home.setGeometry(QtCore.QRect(
            MainWindow.width() - 210, 575, 160, 35))
        self.aboutUs_Home.clicked.connect(self.aboutUsPg)
        self.aboutUs_Home.setStyleSheet(
            "color: #34363a; background-color: #d2c15d; font-size: 20px; font-weight: bold;")

        self.label_14_Home = QtWidgets.QLabel(self.page_Home)
        self.label_14_Home.setGeometry(QtCore.QRect(
            0, self.logoBackground_Home.y() + 215, MainWindow.width(), 55))
        self.label_14_Home.setStyleSheet("font-size: 40px; font-weight: bold;")
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
        self.label_genPas.setPixmap(self.logoPixmap)
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
        self.SettingsBtn_genPas.clicked.connect(self.settingsPg)

        self.AboutUsBtn_genPas = QtWidgets.QPushButton(
            self.layoutWidget_genPas)
        self.AboutUsBtn_genPas.setSizePolicy(sizePolicy)
        self.AboutUsBtn_genPas.setStyleSheet("")
        self.AboutUsBtn_genPas.setObjectName("AboutUsBtn_genPas")
        self.AboutUsBtn_genPas.setProperty("class", "navBar_btn")
        self.AboutUsBtn_genPas.clicked.connect(self.aboutUsPg)
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
        font-size: 45px; font-family: Trebuchet MS; margin-left: 20px; font-weight: bold;""")

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
            font-weight: bold;
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
            ":images/images/Google-Chrome-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chromeButton_genPas.setIcon(icon1_genPas)
        self.chromeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.chromeButton_genPas.setCheckable(True)
        self.chromeButton_genPas.setObjectName("chromeButton_genPas")
        self.chromeButton_genPas.setStyleSheet(self.styleSheet)
        self.FireFoxButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon2_genPas = QtGui.QIcon()
        icon2_genPas.addPixmap(QtGui.QPixmap(
            ":/images/images/Firefox-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FireFoxButton_genPas.setIcon(icon2_genPas)
        self.FireFoxButton_genPas.setCheckable(True)
        self.FireFoxButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.FireFoxButton_genPas.setObjectName("FireFoxButton_genPas")
        self.FireFoxButton_genPas.setStyleSheet(self.styleSheet)
        self.MicrosoftEdgeButton_genPas = QtWidgets.QPushButton(
            self.groupBox_genPas)
        icon3_genPas = QtGui.QIcon()
        icon3_genPas.addPixmap(QtGui.QPixmap(
            ":images/images/icons8-microsoft-edge-144.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MicrosoftEdgeButton_genPas.setIcon(icon3_genPas)
        self.MicrosoftEdgeButton_genPas.setIconSize(QtCore.QSize(40, 40))
        self.MicrosoftEdgeButton_genPas.setCheckable(True)
        self.MicrosoftEdgeButton_genPas.setObjectName(
            "MicrosoftEdgeButton_genPas")
        self.MicrosoftEdgeButton_genPas.setStyleSheet(self.styleSheet)
        self.OperaButton_genPas = QtWidgets.QPushButton(self.groupBox_genPas)
        icon4_genPas = QtGui.QIcon()
        icon4_genPas.addPixmap(QtGui.QPixmap(
            ":images/images/Opera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        font.setPointSize(19)
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
            QtCore.QRect(23, 10, 500, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_selectPreference_genPas.setText("Select Number of Words in Passphrase")
        self.label_selectPreference_genPas.setMinimumHeight(60)
        self.label_selectPreference_genPas.setFont(font)
        self.label_selectPreference_genPas.setAutoFillBackground(True)
        self.label_selectPreference_genPas.setObjectName(
            "label_selectPreference_genPas")
        self.label_selectPreference_genPas.setStyleSheet(self.styleSheet)

        self.comboBox_Number_2_genPas = QtWidgets.QComboBox(
            self.container_2_genPas)
        self.comboBox_Number_2_genPas.setGeometry(QtCore.QRect(
            round((self.scrollArea_genPas.width()-400)/2), 100, 400, 60))
        self.comboBox_Number_2_genPas.setMinimumHeight(50)
        self.comboBox_Number_2_genPas.setEnabled(True)
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

        #a list of created widgets that displays the generated passphrase
        self.resultWidgetList = []

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
        self.label_vault = QtWidgets.QLabel(self.groupBox_logoBackground_vault)
        self.label_vault.setGeometry(QtCore.QRect(round((MainWindow.width(
        ) - 500) / 2), round((self.groupBox_logoBackground_vault.height() - 150)/2), 500, 150))
        self.label_vault.setStyleSheet("")
        self.label_vault.setPixmap(self.logoPixmap)
        self.label_vault.setScaledContents(True)
        self.label_vault.setObjectName("label_vault")
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
        self.SettingsBtn_vault.clicked.connect(self.settingsPg)
        self.AboutUsBtn_vault = QtWidgets.QPushButton(self.layoutWidget_vault)

        self.AboutUsBtn_vault.setSizePolicy(sizePolicy)
        self.AboutUsBtn_vault.setStyleSheet("")
        self.AboutUsBtn_vault.setObjectName("AboutUsBtn_vault")
        self.AboutUsBtn_vault.setProperty("class", "navBar_btn")
        self.AboutUsBtn_vault.clicked.connect(self.aboutUsPg)
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

        #list of website names
        self.widget_names = []
        
        #an array of created custom group box
        self.widgets = []

        #bool to check if user change info
        self.infoChanged = False

        self.styleSheet = """
            font-size: 35px;
            color: #d2c15d;
            font-weight: bold;
        """

        self.welcomeSign = QtWidgets.QWidget()
        self.wcs_layout = QtWidgets.QHBoxLayout(self.welcomeSign)
        self.welcome = QtWidgets.QLabel("Welcome to The Vault!")
        self.welcome.setStyleSheet(self.styleSheet)
        self.addNewAcc = QtWidgets.QPushButton("Add New Account")
        self.addNewAcc.setObjectName("addNewAcc")
        self.addNewAcc.setStyleSheet(self.styleSheet)
        self.addNewAcc.clicked.connect(self.ADD_Account)
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
        border-style: none; padding-left: 10px; color: white; font-weight: bold;
        """)
        sizePolicy.setHeightForWidth(
            self.searchbar.sizePolicy().hasHeightForWidth())


        self.verticalLayout_vault.addWidget(self.groupBox_searchbar_vault)

        spacer_vault = QtWidgets.QSpacerItem(
            1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_vault.addItem(spacer_vault)

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
        self.label_audit.setPixmap(self.logoPixmap)
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
        self.SettingsBtn_audit.clicked.connect(self.settingsPg)
        self.AboutUsBtn_audit = QtWidgets.QPushButton(
            self.layoutWidget_1_audit)
        self.AboutUsBtn_audit.setProperty("class", "navBar_btn")
        self.AboutUsBtn_audit.clicked.connect(self.aboutUsPg)
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
            round((self.stackedWidget.width() - 600) / 2), 350, 600, 500))
        self.securityAuditWidget.setStyleSheet("""
            QWidget{
                border: 2px solid white;
            }
        """)
        font.setPointSize(18)

        self.passwordStrengthAuditLabel = QtWidgets.QLabel("Please enter a password below: ", self.page_audit)
        self.passwordStrengthAuditLabel.setMaximumHeight(60)
        self.passwordStrengthAuditLabel.setFont(font)
        self.passwordStrengthAuditLabel.setStyleSheet("""
            border-style: none;
            border: 0px;
            font-size: 30px;
        """)
        self.saWidgetLayout.addWidget(self.passwordStrengthAuditLabel)

        self.passwordStrengthAuditLE = QtWidgets.QLineEdit(self.page_audit)
        self.passwordStrengthAuditLE.setMinimumHeight(60)
        self.passwordStrengthAuditLE.setFont(font)
        
        self.saWidgetLayout.addWidget(self.passwordStrengthAuditLE)
        
        self.submitBtn = QtWidgets.QPushButton("Submit", self.page_audit)
        self.submitBtn.clicked.connect(self.checkPwdStrength)
        self.submitBtn.setMinimumHeight(60)
        self.submitBtn.setMaximumWidth(240)
        self.submitBtn.setStyleSheet("""
            QPushButton {
                background-color: #d2c15d;
                border-style: none;
                border: 0px;
            }

            QPushButton:hover{
                background-color: #476e9e;
            }
        
        """)
        self.saWidgetLayout.addWidget(self.submitBtn)

        self.displayResultArea  = QtWidgets.QPlainTextEdit(self.page_audit)
        self.displayResultArea.setGeometry(QtCore.QRect(560, 350, 850, 500))
        self.displayResultArea.setReadOnly(True)
        self.displayResultArea.setFont(font)
        self.displayResultArea.insertPlainText("")
        self.displayResultArea.setHidden(True)
        self.displayResultArea.setStyleSheet("""
            background-color: #d2c15d;
            border: 10px outset #d2c15d;
            padding-left: 5px;
        """)
    
        self.stackedWidget.addWidget(self.page_audit)

################################# AboutUs page ####################################
        self.page_aboutUs = QtWidgets.QWidget()
        self.page_aboutUs.setObjectName("page_aboutUs")

        pageAU = Ui_AboutUs()
        pageAU.setupUi(self.page_aboutUs, self.homePg, self.vaultPg, self.settingsPg) 
    
        self.stackedWidget.addWidget(self.page_aboutUs)

################################# Settings page ####################################
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setObjectName("page_settings")

        pageSettings = Ui_Settings()
        pageSettings.setupUi(self.page_settings, self.homePg, self.vaultPg, self.aboutUsPg, self.resetVault, self.resetWordlist)

        self.stackedWidget.addWidget(self.page_settings)

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
            _translate("MainWindow", "2. Access My Vault"))
        self.label_vaultDescription_Home.setText(_translate(
            "MainWindow", "View & add passwords into your vault"))
        self.label_audit_Home.setText(
            _translate("MainWindow", "3. Security Audit"))
        self.label_auditDescription_Home.setText(_translate(
            "MainWindow", "Assess the security of your passwords and passphrases"))
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
            _translate("MainWindow", "Select browser(s)"))
     
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
     
        self.dummyLabel_1_genPas.setText(_translate("MainWindow", ""))
     
        self.dummyLabel_2_genPas.setText(_translate("MainWindow", ""))
    
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

    # redirect user to home page
    def homePg(self):
        self.stackedWidget.setCurrentIndex(0)

    # redirect user to generator page
    def genPasPg(self):
        self.stackedWidget.setCurrentIndex(1)


    # perform an authentication process before letting user get 
    # into vault page and redirect user to vault page 
    # if user is authenticated
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

        vault_db = Vault()

        vault_db_filename = os.path.expanduser('~\Documents\ezPass\\vault')

         #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')

        #if ezPass folder is not exist or vault file is not exist
        if (not os.path.isdir(folder_path) or not os.path.isfile(vault_db_filename)):
            print("test")
            checkPassword = False

            if (not os.path.isdir(folder_path)):
                #create ezPass user password folder
                os.mkdir(folder_path)
               
            #change directory to folder path
            os.chdir(folder_path)   
            #create a setup master password form 
            setupPassword = setupPasForm()
            
            # while the passwords entered are not the same and the user 
            # did not cancel the setup
            while (checkPassword != True and popWindow): 
                # if user clicked submit get both of the entered password
                if setupPassword.exec_():
                    password = setupPassword.password.text()
                    confirmPass = setupPassword.confirmPass.text()
                    #check if they are the same
                    if (password == confirmPass and password != "" and len(password) >= 8):
                        #open a file to record the password
                        vault_db.create_vault(password, vault_db_filename)
                        checkPassword = True

                    else:
                        Dialog = QtWidgets.QDialog()
                        ui = Ui_Dialog()
                        if(len(password) < 8):
                            ui.setupUi(Dialog, "Password must be longer than 8 characters!")
                        else:
                            ui.setupUi(Dialog, "Please try again!")    
                        Dialog.show()
                        Dialog.exec_()
                
                #user cancel the setup 
                else:
                    popWindow = False
                

            if (checkPassword):
                self.stackedWidget.setCurrentIndex(2)  
                
            

        else:
            if(self.authenticateActionVault() is not None):
                 
                #stores all the accounts and info 
                self.parameters = vault_db.get_accounts()
            
                spacer_vault = QtWidgets.QSpacerItem(
                1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)

                 # to maintain the positions of each items inside the layout
                self.verticalLayout_vault.addItem(spacer_vault)
                
                # Iterate the names, creating a new customGroupBox for
                # each one, adding it to the layout and
                # storing a reference in the 'self.widgets' dict
                for x in self.parameters:
                    id = x[0]
                    website = x[1]
                    username = x[2]
                    item = customGroupBox(website, username, id)
                    item.viewDetails(self.viewAccountPwd)
                    item.setContentsMargins(0, 10, 0, 20)
                
                    if (len(self.widgets) != len(self.parameters)):
                        self.verticalLayout_vault.addWidget(item)
                        self.widgets.append(item)
                    if website not in self.widget_names:
                        self.widget_names.append(website)

                self.completer_vault = QtWidgets.QCompleter(self.widget_names)
                self.completer_vault.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
                self.searchbar.setCompleter(self.completer_vault)
                self.stackedWidget.setCurrentIndex(2)

    #authenticate user when they wants to perform user privacy related
    # action  (vault page function)
    def authenticateActionVault(self):
        #create a enter vault password window
        enterVault = vaultPassword()
        checkEnterPassword = False
        popEnterPass = True

        vault_db = Vault()

        #vault db file path
        vault_db_filename = os.path.expanduser('~\Documents\ezPass\\vault')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        os.chdir(folder_path)

        while ( checkEnterPassword == False and popEnterPass):
            createdPassword = ""
            if enterVault.exec_():
                enteredPassword = enterVault.password.text()
                
                #open db file to read the password
                if(os.path.isfile(vault_db_filename)):
                        
                    if (vault_db.authenticate_user(enteredPassword)):
                        checkEnterPassword = True
                        #return the entered password if it matches
                        return enteredPassword

                    else:
                        Dialog = QtWidgets.QDialog()
                        ui = Ui_Dialog()
                        ui.setupUi(Dialog, "Incorrect Password!")
                        Dialog.show()
                        Dialog.exec_()

            else:
                popEnterPass = False
                return None

    # redirect user to 'audit' page    
    def auditPg(self):
        self.stackedWidget.setCurrentIndex(3)

    # redirect user to 'about us' page
    def aboutUsPg(self):
        self.stackedWidget.setCurrentIndex(4)

    # redirect user to 'settings' page
    def settingsPg(self):
        self.stackedWidget.setCurrentIndex(5)

    # if user input can be found inside the list
    # show the widget (groupbox) (vault page function)
    def update_display(self, text):

        for widget in self.widgets:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()

    # create a page according to the provided info from an 
    # created account. (vault page function)
    def viewAccountPwd(self, username, account, id):
        # get the masterpassword returned from 
        # authentication function before entering 
        # the page
        masterpwd = self.authenticateActionVault()
        if (masterpwd is not None):
            self.page_dynamic = QtWidgets.QWidget()
            self.logoBackground_dynamic = QtWidgets.QLabel(self.page_dynamic)
            self.logoBackground_dynamic.setGeometry(
                QtCore.QRect(0, 0, self.stackedWidget.width(), 250))
            self.logoBackground_dynamic.setProperty(
                "class", "logoBackground_genPas")
        
            self.label_dynamic = QtWidgets.QLabel(self.page_dynamic)
            self.label_dynamic.setGeometry(QtCore.QRect(
                round((self.stackedWidget.width() - 560) / 2), 30, 560, 150))
            self.label_dynamic.setPixmap(self.logoPixmap)
            self.label_dynamic.setScaledContents(True)
            self.label_dynamic.setAlignment(QtCore.Qt.AlignCenter)
            self.label_dynamic.setObjectName("label_dynamic")
            self.label_dynamic.setProperty("class", "label_logo")

            self.backButton = QtWidgets.QPushButton(" <-- Back to vault", self.page_dynamic)
            self.backButton.setGeometry(QtCore.QRect(round((self.stackedWidget.width() - 300) / 2), 840, 300, 60))
            self.backButton.clicked.connect(self.backToVault)
            self.backButton.setObjectName("backVaultBtn")    
            self.layoutWidget_1_dynamic = QtWidgets.QWidget(self.page_dynamic)
            self.layoutWidget_1_dynamic.setGeometry(QtCore.QRect(
                0, self.logoBackground_dynamic.height() - 30, self.stackedWidget.width(), 100))
            self.layoutWidget_1_dynamic.setProperty("class", "navBar_genPas")

            self.HomeBtn_dynamic = QtWidgets.QPushButton(
                self.layoutWidget_1_dynamic)
            self.HomeBtn_dynamic.setProperty("class", "navBar_btn")
            self.HomeBtn_dynamic.setText("Home")
            self.HomeBtn_dynamic.clicked.connect(self.homePg)
            self.SettingsBtn_dynamic = QtWidgets.QPushButton(
                self.layoutWidget_1_dynamic)
            self.SettingsBtn_dynamic.setProperty("class", "navBar_btn")
            self.SettingsBtn_dynamic.setText("Settings")
            self.SettingsBtn_dynamic.clicked.connect(self.settingsPg)
            self.AboutUsBtn_dynamic = QtWidgets.QPushButton(
                self.layoutWidget_1_dynamic)
            self.AboutUsBtn_dynamic.setProperty("class", "navBar_btn")
            self.AboutUsBtn_dynamic.setText("About Us")
            self.AboutUsBtn_dynamic.clicked.connect(self.aboutUsPg)
            self.dummyLabel_3_dynamic = QtWidgets.QLabel(
                self.layoutWidget_1_dynamic)
            self.dummyLabel_3_dynamic.setProperty("class", "QLabel_genPas")
            self.dummyLabel_4_dynamic = QtWidgets.QLabel(
                self.layoutWidget_1_dynamic)
            self.dummyLabel_4_dynamic.setProperty("class", "QLabel_genPas")

            self.navBar_dynamic = QtWidgets.QHBoxLayout(self.layoutWidget_1_dynamic)
            self.navBar_dynamic.addWidget(self.HomeBtn_dynamic)
            self.navBar_dynamic.addWidget(self.SettingsBtn_dynamic)
            self.navBar_dynamic.addWidget(self.AboutUsBtn_dynamic)
            self.navBar_dynamic.addWidget(self.dummyLabel_3_dynamic)
            self.navBar_dynamic.addWidget(self.dummyLabel_4_dynamic)

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
            self.accountLabel_dynamic.setStyleSheet("""
                border-style: none;
                font-size: 40px;
                font-weight: bold;
                color: #ffffff;
            """)
            #self.accountLabel_dynamic.setProperty("class", "labels_dynamic")
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

            vault = Vault()
            self.pwdLE_dynamic = QtWidgets.QLineEdit(vault.view_password(id, masterpwd))
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
            self.delBtn_dynamic.clicked.connect(lambda: self.deleteAcc(id))
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
            self.saveBtn_dynamic.clicked.connect(lambda: self.saveInfo(id, account, masterpwd))
            self.checkPasswordStrengthBtn = QtWidgets.QPushButton("Audit password", self.groupBox_dynamic)
            self.checkPasswordStrengthBtn.setGeometry(QtCore.QRect(self.groupBox_dynamic.width() - 900, self.groupBox_dynamic.height() - 80, 240, 60))
            self.checkPasswordStrengthBtn.clicked.connect(lambda: self.auditPasswordfromVault(self.pwdLE_dynamic.text()))
            self.checkPasswordStrengthBtn.setStyleSheet(self.styleSheet)
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

    # let users copy the text by pressing the copy button
    @QtCore.pyqtSlot()
    def copyText(self, pwd):
        self.qclip.setText(pwd)


    # set most of the buttons to be disabled and 
    # enable both password and username field (vault page function)
    def editInfo(self):
        # store both username and password to be used later 
        # when user leave one of the field blank 
        self.previousUserName = self.userNameLE_dynamic.text()
        self.previousPassword = self.pwdLE_dynamic.text()

        self.copyBtn_dynamic.setDisabled(True)
        self.pwdLE_dynamic.setDisabled(False)
        self.userNameLE_dynamic.setDisabled(False)
        self.pwdLE_dynamic.setStyleSheet(
            """background-color: white; color: black;""")
        self.userNameLE_dynamic.setStyleSheet(
            """background-color: white; color: black;""")
        self.editBtn_dynamic.setDisabled(True)
        self.saveBtn_dynamic.setDisabled(False)

    # user click save button to save the corresponding data
    # to database
    def saveInfo(self, id, account, masterpwd):
        vault = Vault
        self.copyBtn_dynamic.setDisabled(False)
        self.pwdLE_dynamic.setDisabled(True)
        self.userNameLE_dynamic.setDisabled(True)
        self.pwdLE_dynamic.setStyleSheet(
            """background-color: #34363a; color:white; border-style: none;""")
        self.userNameLE_dynamic.setStyleSheet(
            """background-color: #34363a; color:white; border-style: none;""")
        self.editBtn_dynamic.setDisabled(False)
        self.saveBtn_dynamic.setDisabled(True)

        userName = self.userNameLE_dynamic.text()
        password = self.pwdLE_dynamic.text()

        # if either username or passowrd is empty
        # prompt a window to alert user
        if (userName == "" or password == ""):
            self.userNameLE_dynamic.setText(self.previousUserName)
            self.pwdLE_dynamic.setText(self.previousPassword)
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog, "Username and password cannot be empty")
            Dialog.show()
            Dialog.exec_()
            self.infoChanged = False

        # else save it into database and add a group box with 
        # corresponding data into vault page
        else:
            vault = Vault()
            vault.edit_account(id, account, self.userNameLE_dynamic.text())
            vault.edit_account_password(id, self.pwdLE_dynamic.text(), masterpwd)
            
            for x in self.widgets:
                if x.id == id:
                    #update object attributes in self.widgets
                    x.name = self.userNameLE_dynamic.text()
                    #remove the widget from vault page (update display)
                    x.hide()
                    self.verticalLayout_vault.removeWidget(x)
                    item = customGroupBox(account, x.name, id)
                    item.viewDetails(self.viewAccountPwd)
                    self.widgets.pop(self.widgets.index(x))
                    self.widgets.append(item)
                    
                    self.verticalLayout_vault.addWidget(item)
                    
            self.infoChanged = True
        
    # a function that create Pop up windows when user deletes an
    # account from vault page, and remove the related groupbox 
    # from vault page
    def deleteAcc(self, id):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, "Confirm deletion of account?")
        Dialog.show()
        vault = Vault()
        

        if Dialog.exec_(): 
            
            for i in self.widgets:
                if (i.id == id):
                    i.hide()
                    self.verticalLayout_vault.removeWidget(i)
                    self.widget_names.remove(i.name)
                    self.widgets.pop(self.widgets.index(i))
                    self.completer_vault = QtWidgets.QCompleter(self.widget_names)
                    self.completer_vault.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
                    self.searchbar.setCompleter(self.completer_vault)
                         
            vault.delete_account(id)

            #self.parameters = vault.get_accounts()
            self.stackedWidget.setCurrentIndex(2)
            

        else:
            print("Cancel!")

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
            

    #show the preferences comboboxes including starting alphabets
    # and number/symbols at the bottom of genPas page (generator page function)
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
        self.generalLabel_genPas = QtWidgets.QWidget()
        self.generalLabel_Hlayout_genPas = QtWidgets.QHBoxLayout(self.generalLabel_genPas)
        self.preference_Label_genPas = QtWidgets.QLabel()
        self.preference_Label_genPas.setText("Select Preferred Alphabet")
        self.preference_Label_genPas.setMaximumWidth(300)
        self.reminder_1_genPas = QtWidgets.QLabel("(you may leave this blank)")
        self.reminder_1_genPas.setStyleSheet("font-size: 18px;")
        self.generalLabel_Hlayout_genPas.addWidget(self.preference_Label_genPas)
        self.generalLabel_Hlayout_genPas.addWidget(self.reminder_1_genPas)
        self.cb_dynamic_Vlayout.addWidget(self.generalLabel_genPas)
        
        
        self.cb_dynamic_Hlayout = QtWidgets.QHBoxLayout()
        self.cb_2_dynamic = QtWidgets.QGroupBox()
        self.cb_dynamic_2_Hlayout = QtWidgets.QHBoxLayout(self.cb_2_dynamic)

        self.cb_dynamic_symbol = QtWidgets.QGroupBox()
        self.cb_dynamic_symbol_layoutWidget = QtWidgets.QWidget()
        self.cb_dynamic_symbol_Vlayout = QtWidgets.QVBoxLayout(
            self.cb_dynamic_symbol)
        self.generalLabel_2_genPas = QtWidgets.QWidget()   
        self.generalLabel_2_Hlayout_genPas = QtWidgets.QHBoxLayout(self.generalLabel_2_genPas)
        self.preference_Label_symbol_genPas = QtWidgets.QLabel()
        self.preference_Label_symbol_genPas.setText(
            "Select Preferred Symbol / Number")
        self.preference_Label_symbol_genPas.setMaximumWidth(385)
        self.reminder_2_genPas = QtWidgets.QLabel("(you may leave this blank)")
        self.reminder_2_genPas.setStyleSheet("font-size: 18px;")
        self.generalLabel_2_Hlayout_genPas.addWidget(self.preference_Label_symbol_genPas)
        self.generalLabel_2_Hlayout_genPas.addWidget(self.reminder_2_genPas)


        self.cb_dynamic_symbol_Vlayout.addWidget(self.generalLabel_2_genPas)
        self.cb_dynamic_symbol_Hlayout = QtWidgets.QHBoxLayout()
        self.cb_2_dynamic_symbol = QtWidgets.QGroupBox()
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


        # if length of number of words combo box == 1
        # the only option that length != 1 is the display text
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

            # add a spacer to adjust the spacing between combo boxes according to
            # number of word chosen by user to create a passphrase
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

    # crete an extra row of elements that are used to 
    # display the generated passphrase and also call the 
    # generator to generate passphrase  (generator page function)   
    def genPassword(self):

        self.styleSheet = """ 
            QPushButton {
                background-color: #d2c15d;
                font-size: 30px;
                border-radius: 20px;
                margin-left: 40px;
            }

            QLabel {
                font-size: 25px;
                font-weight: bold;
            }

        """
        # self.generatePasswordButton.setDisabled(True)
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
        self.resetAllbtn.setFixedSize(250, 150)
        self.resetAllbtn.clicked.connect(self.resetAll)
        self.copyPassPhrasebtn = QtWidgets.QPushButton("Copy")
        self.copyPassPhrasebtn.setStyleSheet(self.styleSheet)
        self.copyPassPhrasebtn.setFixedSize(180, 150)
        self.copyPassPhrasebtn.clicked.connect( lambda: self.copyText(self.finalResult.text()))
        self.displayText = QtWidgets.QLabel("Generated passphrase: ")
        self.displayText.setStyleSheet("font-size: 30px")
        # if Opera browser is opened and running at the background
        # prompt user to inform them to close the browser
        if(check_running_process('opera') and ('Opera') in self.btnList):
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog, "Please exit all opera processes and try again.")
            Dialog.show()
            Dialog.exec_()

        # if Microsoft Edge browser is opened and running at the background
        # prompt user to inform them to close the browser
        elif(check_running_process('msedge') and ('Microsoft Edge') in self.btnList):
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog, "Please exit all Microsoft Edge processes and try again.")
            Dialog.show()
            Dialog.exec_()

        # if Firefox browser is opened and running at the background
        # prompt user to inform them to close the browser
        elif(check_running_process('firefox') and ('Firefox') in self.btnList):
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog, "Please exit all firefox processes and try again.")
            Dialog.show()
            Dialog.exec_()

        # if Chrome browser is opened and running at the background
        # prompt user to inform them to close the browser
        elif(check_running_process('chrome') and ('Google Chrome') in self.btnList):
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog, "Please exit all chrome processes and try again.")
            Dialog.show()
            Dialog.exec_()

        # call generate password function to get the passprhase
        else:
            self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap(':/images/images/splash.png'))

            self.splash.move(300,350)

            self.splash.show()
            
            password_generator = Password_Generator()
            self.finalResult.setText(password_generator.generate_password(self.btnList, int(
                self.comboBox_wordNo), self.preferenceList))

            QtCore.QTimer.singleShot(800, self.splash.close)

            self.resultWidget_HLayout.addWidget(self.displayText)
            self.resultWidget_HLayout.addWidget(self.finalResult)
            self.resultWidget_HLayout.addWidget(self.copyPassPhrasebtn)
            self.resultWidget_HLayout.addWidget(self.resetAllbtn)
            
            if (len(self.resultWidgetList) == 0):
                self.resultWidgetList.append(self.resultLayoutWidget)
                self.verticalLayout_genPas.addWidget(self.resultWidgetList[0])
                
            else:
                self.verticalLayout_genPas.removeWidget(self.resultWidgetList[0])
                self.resultWidgetList.pop(0)
                self.resultWidgetList.append(self.resultLayoutWidget)
                self.verticalLayout_genPas.addWidget(self.resultWidgetList[0])
            
    # User is not allowed to choose another number of word in passphrase 
    # until the click reset number button,
    # the page will remove previously created elements.
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

    # set the buttons to be editable / clickable again when user click 
    # 'reset all' button and also remove the previously created 
    # preference combo boxes  (generator page function)
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
    # (generator page function)
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
    # buttons & combo boxes to be editable again (generator page function)
    def resetAll(self):
        self.comboBox_Number_2_genPas.setEnabled(True)
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

    # get user back to vault page (vault page function)
    def backToVault(self):  

        self.stackedWidget.setCurrentIndex(2)

    # add an account into the vault page and database (vault page function)
    def ADD_Account(self):
        addAccount = createAccountForm()
        spacer_vault = QtWidgets.QSpacerItem(
            1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vault = Vault()
        continueCreateAcc = True

        popWindow = True
        #get the masterPassword from authentication process
        masterPassword = self.authenticateActionVault()

        if(masterPassword is not None):
            
            # while user with to continue adding an account
            # and clicked ok button when the error window pops up
            while (continueCreateAcc and popWindow):
                if addAccount.exec_():
                    website = addAccount.website.text()
                    username = addAccount.username.text()
                    password = addAccount.password.text()

                    # if all the fields are filled
                    if ( website != "" and username != "" and password != ""):

                        #add an account to database
                        account_id = vault.add_account(website, password, username, masterPassword)

                        
                        #create a groupbox to display on gui
                        item = customGroupBox(website, username, account_id)
                        item.viewDetails(self.viewAccountPwd)
                        item.setContentsMargins(0, 10, 0, 20)
                        self.verticalLayout_vault.addWidget(item)
                        self.widgets.append(item)
                        self.verticalLayout_vault.addItem(spacer_vault)

                        if website not in self.widget_names:
                            self.widget_names.append(website)
                            self.completer_vault = QtWidgets.QCompleter(self.widget_names)
                            self.completer_vault.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
                            self.searchbar.setCompleter(self.completer_vault)

                        continueCreateAcc = False
                        
                    # else prompt a window to alert user that 
                    # the fields cannot be empty
                    else: 
                        Dialog = QtWidgets.QDialog()
                        ui = Ui_Dialog()
                        ui.setupUi(Dialog, "Information insufficient!")
                        Dialog.show()
                        if Dialog.exec_():
                            pass
                        else:
                            popWindow = False

                else:
                    continueCreateAcc = False
            
    # check the strength of the provided password (audit page function)
    def checkPwdStrength(self):
        userInput = self.passwordStrengthAuditLE.text()
        resultString = ''
        tempFeedback = ''
        scoreResult = ''

        self.securityAuditWidget.setGeometry(QtCore.QRect(
            30, 350, 500, 500))

        self.displayResultArea.setHidden(False)
        refreshString = self.displayResultArea.toPlainText()
        
        if refreshString != "":
            self.displayResultArea.clear()

        if (userInput != ''):
            result = zxcvbn(self.passwordStrengthAuditLE.text())
            if (result['score'] == 0):
                scoreResult = "Your password score: 0 / 4 Extremely Weak\n"

            if (result['score'] == 1):
                scoreResult = "Your password score: 1 / 4 Poor\n"

            elif (result['score'] == 2):
                scoreResult = "Your password score: 2 / 4 Moderate\n"   

            elif (result['score'] == 3):
                scoreResult = "Your password score: 3 / 4 Good\n"

            elif (result['score'] == 4):
                scoreResult = "Your password score: 4 / 4 Strong\n"
            
            guessesResult = "Guesses: " + str(result['guesses']) + "\n"

            
            for i in result['feedback']['suggestions']:
                tempFeedback = str(i) + " "

            
            feedback = "Feedback: " + tempFeedback


            if tempFeedback != '': 
                resultString = scoreResult + "\n" + guessesResult + "\n" + feedback
                self.displayResultArea.insertPlainText(resultString)
            else:
                resultString = scoreResult + "\n" + guessesResult
                self.displayResultArea.insertPlainText(resultString)

        else:
            self.displayResultArea.insertPlainText("Please enter a password.")

    # user can click audit password from each account page to 
    # get the password directly to audit page to check (audit page function)  
    def auditPasswordfromVault(self, password):
        self.stackedWidget.setCurrentIndex(3)

        self.passwordStrengthAuditLE.setText(password)

        self.checkPwdStrength()

    # user click reset vault button to delete the entire database 
    # (settings page function)
    def resetVault(self):
        folder_path = os.path.expanduser('~\Documents\ezPass')
        vault_db_filename = os.path.expanduser('~\Documents\ezPass\\vault')
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, "Confirm deletion of content of the vault?")
        Dialog.show()
        # if user clicked confirm, the program will delete the file
        if Dialog.exec_():
            #if the ezPass folder and vault file exists 
            if(os.path.isdir(folder_path) and os.path.isfile(vault_db_filename)):
                vault = "vault"
                file_path = os.path.join(folder_path, vault)
                os.remove(file_path)
                for x in self.widgets:
                    x.setHidden(True)
                    self.verticalLayout_vault.removeWidget(x)
                    x.delete()
                    self.widgets.pop(self.widgets.index(x))

            #else prompt user a window to inform user 
            else:
                Dialog_noFileFound = QtWidgets.QDialog()
                ui_noFileFound = Ui_Dialog()
                ui_noFileFound.setupUi(Dialog_noFileFound, "Vault file does not exist")
                Dialog_noFileFound.show()
                Dialog_noFileFound.exec_()
        
        # else dont do anything
        else: 
            pass

    # user click reset to delete the wordlist folders (settings page function)
    def resetWordlist(self):
        logs_folder_path = os.path.expanduser('~\Documents\ezPass\Logs')

        keywords_folder_path = os.path.expanduser('~\Documents\ezPass\Keywords')

        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, "Confirm deletion of generated wordlist?")
        Dialog.show()
        if Dialog.exec_():
            if(os.path.isdir(logs_folder_path) and os.path.isdir(keywords_folder_path)):
                shutil.rmtree(logs_folder_path)
                shutil.rmtree(keywords_folder_path)
        
            else: 
                Dialog_noFileFound = QtWidgets.QDialog()
                ui_noFileFound = Ui_Dialog()
                ui_noFileFound.setupUi(Dialog_noFileFound, "Wordlist file is already deleted.")
                Dialog_noFileFound.show()
                Dialog_noFileFound.exec_()

        else:
            pass




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
    
        QPushButton#backVaultBtn  {
            background-color: #34363a;
            font-size: 25px;
            color: white;
            border-style: none;
        }

        QPushButton#backVaultBtn:hover {
            color: red;
        }

    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
