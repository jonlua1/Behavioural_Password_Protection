import resource
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings, homeFunc, vaultFunc, aboutUsFunc, resetVaultFunc):
        
        self.layoutWidget = QtWidgets.QWidget(Settings)
        self.layoutWidget.setGeometry(QtCore.QRect(0,0,1500,900))
     
        self.groupBox_logoBackground = QtWidgets.QGroupBox(
            self.layoutWidget)
        self.groupBox_logoBackground.setMaximumHeight(250)
        self.groupBox_logoBackground.setStyleSheet("background-color: #454547;")
        self.groupBox_logoBackground.setTitle("")
        self.groupBox_logoBackground.setObjectName("groupBox")
        self.label_backgroundLogo = QtWidgets.QLabel(self.groupBox_logoBackground)
        self.label_backgroundLogo.setGeometry(QtCore.QRect(round((self.layoutWidget.width(
        ) - 500) / 2), round((self.groupBox_logoBackground.height() + 75) /2), 500, 150))
        self.label_backgroundLogo.setStyleSheet("")
        self.label_backgroundLogo.setPixmap(QtGui.QPixmap(":/images/images/ezPassLogo.PNG"))
        self.label_backgroundLogo.setScaledContents(True)
        self.label_backgroundLogo.setObjectName("label_backgroundLogo")
       
        self.layoutWidget_1 = QtWidgets.QWidget(self.layoutWidget)
        self.layoutWidget_1.setGeometry(QtCore.QRect(
            0, 250, self.layoutWidget.width(), 100))
        self.layoutWidget_1.setProperty("class", "navBar_genPas")
        self.layoutWidget_1.setMaximumHeight(100)

        self.HomeBtn = QtWidgets.QPushButton("Home", self.layoutWidget_1)
        self.HomeBtn.setProperty("class", "navBar_btn")
        self.HomeBtn.clicked.connect(homeFunc)
        self.VaultBtn = QtWidgets.QPushButton("Vault", self.layoutWidget_1)
        self.VaultBtn.setProperty("class", "navBar_btn")
        self.VaultBtn.clicked.connect(vaultFunc)
        self.SettingsBtn = QtWidgets.QPushButton(
            "Settings", self.layoutWidget_1)
        self.SettingsBtn.setProperty("class", "navBar_btn")
        self.AboutUsBtn = QtWidgets.QPushButton(
            "About Us", self.layoutWidget_1)
        self.AboutUsBtn.setProperty("class", "navBar_btn")
        self.AboutUsBtn.clicked.connect(aboutUsFunc)
        self.dummylabel_logo_3= QtWidgets.QLabel(self.layoutWidget_1)
        self.dummylabel_logo_3.setProperty("class", "QLabel_genPas")
        self.dummylabel_logo_4 = QtWidgets.QLabel(self.layoutWidget_1)
        self.dummylabel_logo_4.setProperty("class", "QLabel_genPas")

        self.removeVaultFileBtn = QtWidgets.QPushButton("Reset Vault", self.layoutWidget)
        self.removeVaultFileBtn.setGeometry(QtCore.QRect(round((self.layoutWidget.width() - 400) / 2),
            700, 400, 100
        ))
        self.removeVaultFileBtn.clicked.connect(resetVaultFunc)

        self.navBar = QtWidgets.QHBoxLayout(self.layoutWidget_1)
        self.navBar.addWidget(self.HomeBtn)
        self.navBar.addWidget(self.VaultBtn)
        self.navBar.addWidget(self.SettingsBtn)
        self.navBar.addWidget(self.AboutUsBtn)
        self.navBar.addWidget(self.dummylabel_logo_3)
        self.navBar.addWidget(self.dummylabel_logo_4)

    

    