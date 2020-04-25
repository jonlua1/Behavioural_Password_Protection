# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, round(MainWindow.height() * 0.3), MainWindow.width(), round(MainWindow.height() * 0.7)))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")

        self.backgroundWidget = QtWidgets.QLabel(self.groupBox)
        self.backgroundWidget.setGeometry(0, 0, self.groupBox.width(), self.groupBox.height())
        self.backgroundWidget.setStyleSheet(" background-color: #d2c15d;")
 
        self.pbHeight = round(self.groupBox.height() * 0.28)
        self.pbWidth = self.groupBox.width() - 100;

        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), 10, self.pbWidth, self.pbHeight))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.layoutWidget_2.setProperty("class", "layout_Background")
        self.horizontalLayout_GenPass = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_GenPass.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_GenPass.setObjectName("horizontalLayout_GenPass")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), 10, self.pbWidth, self.pbHeight))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setProperty("class", "btn-style")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_genPwd = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_genPwd.setStyleSheet("")
        self.label_genPwd.setObjectName("label_genPwd")
        self.verticalLayout_7.addWidget(self.label_genPwd)
        self.label_genPwdDescription = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_genPwdDescription.setStyleSheet("")
        self.label_genPwdDescription.setObjectName("label_genPwdDescription")
        self.verticalLayout_7.addWidget(self.label_genPwdDescription)
        self.horizontalLayout_GenPass.addLayout(self.verticalLayout_7)
        self.dummy_label1 = QtWidgets.QLabel(self.layoutWidget_2)
        self.dummy_label1.setText("")
        self.dummy_label1.setObjectName("dummy_label1")
        self.horizontalLayout_GenPass.addWidget(self.dummy_label1)
        self.buttonPixmap_Gen = QtWidgets.QLabel(self.layoutWidget_2)
        self.buttonPixmap_Gen.setText("")
        self.buttonPixmap_Gen.setPixmap(QtGui.QPixmap("./images/generate_password.jpg"))
        self.buttonPixmap_Gen.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPixmap_Gen.setObjectName("buttonPixmap_Gen")
        self.horizontalLayout_GenPass.addWidget(self.buttonPixmap_Gen)

        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), self.pbHeight + 20, self.pbWidth, self.pbHeight))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setProperty("class", "layout_Background")
        self.horizontalLayout_vault = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_vault.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_vault.setObjectName("horizontalLayout_vault")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), self.pbHeight + 20, self.pbWidth, self.pbHeight))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setProperty("class", "btn-style")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_vault = QtWidgets.QLabel(self.layoutWidget)
        self.label_vault.setStyleSheet("")
        self.label_vault.setObjectName("label_vault")
        self.verticalLayout_2.addWidget(self.label_vault)
        self.label_vaultDescription = QtWidgets.QLabel(self.layoutWidget)
        self.label_vaultDescription.setStyleSheet("")
        self.label_vaultDescription.setObjectName("label_vaultDescription")
        self.verticalLayout_2.addWidget(self.label_vaultDescription)
        self.horizontalLayout_vault.addLayout(self.verticalLayout_2)
        self.dummy_label2 = QtWidgets.QLabel(self.layoutWidget)
        self.dummy_label2.setStyleSheet("")
        self.dummy_label2.setText("")
        self.dummy_label2.setObjectName("dummy_label2")
        self.horizontalLayout_vault.addWidget(self.dummy_label2)
        self.buttonPixmap_Vault = QtWidgets.QLabel(self.layoutWidget)
        self.buttonPixmap_Vault.setText("")
        self.buttonPixmap_Vault.setPixmap(QtGui.QPixmap("./images/smaller_vault.png"))
        self.buttonPixmap_Vault.setScaledContents(True)
        self.buttonPixmap_Vault.setAlignment(QtCore.Qt.AlignCenter)
        self.buttonPixmap_Vault.setObjectName("buttonPixmap_Vault")
        self.horizontalLayout_vault.addWidget(self.buttonPixmap_Vault)

        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(round((MainWindow.width() - self.pbWidth) / 2), self.pbHeight * 2 + 30, self.pbWidth, self.pbHeight))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.layoutWidget_3.setProperty("class", "layout_Background")
        self.horizontalLayout_audit = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_audit.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_audit.setObjectName("horizontalLayout_audit")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), self.pbHeight * 2 + 30, self.pbWidth, self.pbHeight))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setProperty("class", "btn-style")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_audit = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_audit.setStyleSheet("")
        self.label_audit.setObjectName("label_audit")
        self.verticalLayout_3.addWidget(self.label_audit)
        self.label_auditDescription = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_auditDescription.setStyleSheet("")
        self.label_auditDescription.setObjectName("label_auditDescription")
        self.verticalLayout_3.addWidget(self.label_auditDescription)
        self.horizontalLayout_audit.addLayout(self.verticalLayout_3)
        self.dummy_label3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.dummy_label3.setStyleSheet("")
        self.dummy_label3.setText("")
        self.dummy_label3.setObjectName("dummy_label3")
        self.horizontalLayout_audit.addWidget(self.dummy_label3)
        self.buttonPixmap_audit = QtWidgets.QLabel(self.layoutWidget_3)
        self.buttonPixmap_audit.setText("")
        self.buttonPixmap_audit.setPixmap(QtGui.QPixmap("./images/security_Audit.jpg"))
        self.buttonPixmap_audit.setObjectName("buttonPixmap_audit")
        self.buttonPixmap_audit.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_audit.addWidget(self.buttonPixmap_audit)

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

        self.settings = QtWidgets.QPushButton(self.groupBox)
        self.settings.setGeometry(QtCore.QRect(MainWindow.width() - 370, 565, 160, 35))
        self.settings.setStyleSheet("color: #34363a; background-color: #d2c15d; font-size: 20px")
        self.aboutUs = QtWidgets.QPushButton(self.groupBox)
        self.aboutUs.setGeometry(QtCore.QRect(MainWindow.width() - 210, 565, 160, 35))
        self.aboutUs.setStyleSheet("color: #34363a; background-color: #d2c15d; font-size: 20px")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(0, self.logoBackground.y()+ 215, MainWindow.width(), 55))
        self.label_14.setStyleSheet("font-size: 30px")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.label_genPwd.setText(_translate("MainWindow", "1. Generate Passphrase"))
        self.label_genPwdDescription.setText(_translate("MainWindow", "Obtain a password using our simple but secure algorithm "))
        self.label_vault.setText(_translate("MainWindow", "2. Access my vault"))
        self.label_vaultDescription.setText(_translate("MainWindow", "View & add passwords into your vault"))
        self.label_audit.setText(_translate("MainWindow", "3. Security Audit"))
        self.label_auditDescription.setText(_translate("MainWindow", "Assess the security of the passwords in your vault"))
        self.label_14.setText(_translate("MainWindow", "Welcome, what would you like to do?"))
        self.settings.setText(_translate("MainWindow", "Settings"))
        self.aboutUs.setText(_translate("MainWindow", "About Us"))

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

        .logoBackground {
            background-color: #454547;
         }
    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
