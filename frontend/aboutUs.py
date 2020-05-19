# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutUs.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import resource
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutUs(object):
    def setupUi(self, AboutUs, homeFunc, vaultFunc, settingsFunc):
        self.homeFunc = homeFunc
        self.vaultFunc = vaultFunc
        AboutUs.setObjectName("AboutUs")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/lock_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutUs.setWindowIcon(icon)
        self.scrollArea = QtWidgets.QScrollArea(AboutUs)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 476, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_logoBackground = QtWidgets.QGroupBox(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
        self.groupBox_logoBackground.sizePolicy().hasHeightForWidth())
        self.groupBox_logoBackground.setSizePolicy(sizePolicy)
        self.groupBox_logoBackground.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_logoBackground.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.groupBox_logoBackground.setStyleSheet(
            "background-color: #454547;")
        self.groupBox_logoBackground.setTitle("")
        self.groupBox_logoBackground.setObjectName("groupBox")
        self.label_backgroundLogo = QtWidgets.QLabel(self.groupBox_logoBackground)
        self.label_backgroundLogo.setGeometry(QtCore.QRect(round((self.scrollArea.width(
        ) - 500) / 2), round((self.groupBox_logoBackground.height() - 150)/2), 500, 150))
        self.label_backgroundLogo.setStyleSheet("")
        self.label_backgroundLogo.setPixmap(QtGui.QPixmap(":/images/images/ezPassLogo.PNG"))
        self.label_backgroundLogo.setScaledContents(True)
        self.label_backgroundLogo.setObjectName("label_backgroundLogo")
        self.verticalLayout.addWidget(self.groupBox_logoBackground)

        self.layoutWidget = QtWidgets.QWidget(
            self.scrollAreaWidgetContents)
        sizePolicy.setHeightForWidth(
            self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.layoutWidget.setStyleSheet("background-color: #d2c15d;")
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setProperty("class", "navBar_genPas")

        self.HomeBtn = QtWidgets.QPushButton("Home", self.layoutWidget)
        self.HomeBtn.setSizePolicy(sizePolicy)
        self.HomeBtn.setStyleSheet("")
        self.HomeBtn.setObjectName("HomeBtn")
        self.HomeBtn.setProperty("class", "navBar_btn")
        self.HomeBtn.clicked.connect(self.homeFunc)

        self.VaultBtn = QtWidgets.QPushButton("Vault", self.layoutWidget)
        self.VaultBtn.setSizePolicy(sizePolicy)
        self.VaultBtn.setStyleSheet("")
        self.VaultBtn.setObjectName("HomeBtn")
        self.VaultBtn.setProperty("class", "navBar_btn")
        self.VaultBtn.clicked.connect(self.vaultFunc)

        self.SettingsBtn = QtWidgets.QPushButton(
            "Settings", self.layoutWidget)
        self.SettingsBtn.setSizePolicy(sizePolicy)
        self.SettingsBtn.setStyleSheet("")
        self.SettingsBtn.setObjectName("SettingsBtn")
        self.SettingsBtn.setProperty("class", "navBar_btn")
        self.SettingsBtn.clicked.connect(settingsFunc)

        self.AboutUsBtn = QtWidgets.QPushButton(
            "About Us", self.layoutWidget)
        self.AboutUsBtn.setSizePolicy(sizePolicy)
        self.AboutUsBtn.setStyleSheet("")
        self.AboutUsBtn.setObjectName("AboutUsBtn")
        self.AboutUsBtn.setProperty("class", "navBar_btn")
        self.dummyLabel_1 = QtWidgets.QLabel(self.layoutWidget)
        self.dummyLabel_1.setProperty("class", "QLabel_genPas")
        self.dummyLabel_1.setStyleSheet("border-style: none;")
        self.dummyLabel_2 = QtWidgets.QLabel(self.layoutWidget)
        self.dummyLabel_2.setProperty("class", "QLabel_genPas")
        self.dummyLabel_2.setStyleSheet("border-style: none;")

        self.navBar = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.navBar.setContentsMargins(20, 0, 0, 0)
        self.navBar.setSpacing(0)
        self.navBar.addWidget(self.HomeBtn)
        self.navBar.addWidget(self.VaultBtn)
        self.navBar.addWidget(self.SettingsBtn)
        self.navBar.addWidget(self.AboutUsBtn)
        self.navBar.addWidget(self.dummyLabel_1)
        self.navBar.addWidget(self.dummyLabel_2)

        self.verticalLayout.addWidget(self.layoutWidget)

        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 1000))
        self.textBrowser.setStyleSheet("""
            padding-left: 20px;
            padding-top: 20px;
            color: #d2c15d;
            background-color: #34363a;
        """)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(AboutUs)
        QtCore.QMetaObject.connectSlotsByName(AboutUs)

    def retranslateUi(self, AboutUs):
        _translate = QtCore.QCoreApplication.translate
        AboutUs.setWindowTitle(_translate("AboutUs", "AboutUs"))
        self.textBrowser.setHtml(_translate("AboutUs", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"color:white; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Welcome to EzPass!</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">EzPass is a simple application that offers a myriad of password-related services. While the Passphrase Generation is the core feature of our application, EzPass do offer other services like secure password storage and a simple password rating feature. Read on to learn more about the application!</span> </p>\n"
"<p style=\"color:white; margin-top:20px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Passphrase Generation</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">Our Passphrase Generation feature is the highlight of our product. EzPass generates passphrases instead of passwords as they provide greater security for our users. More importantly, these passphrases are personalised to our users. EzPass extracts, filtesr and processes your browser history to obtain recurring words to add to a wordlist. The application will retrieve words from these wordlists to form your passphrase.</span> </p>\n"
"<p style=\"color:white; margin-top:20px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Password Vault</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">EzPass offers a vault for the safekeeping of your credentials. You may choose to store both your own passwords as well as the passphrases EzPass generated. Feel free to add, edit and delete any account entries.  EzPass runs entirely on your device and is disconnected from the web. However, we still take measures to ensure your credentials are kept secure and out of the hands of unauthorised personnel.</span> </p>\n"
"<p style=\"color:white; margin-top:20px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Password Audit</span><span style=\" font-size:12pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%;\"><span style=\" font-size:12pt;\">Take advantage of our password audit feature to assess the strength of your own passwords. EzPass lets you know the overall strength of your password and the estimated time for someone to guess your password. If the application rates your password poorly, how about giving our secure generated passphrases a try?</span> </p></body></html>"))

    

    