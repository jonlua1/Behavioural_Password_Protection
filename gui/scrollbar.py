# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrollbar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from customWidget import OnOffWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_vault = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_vault.setGeometry(QtCore.QRect(0, 0, MainWindow.width(), MainWindow.height()))
        self.scrollArea_vault.setStyleSheet("")
        self.scrollArea_vault.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_vault.setWidgetResizable(True)
        self.scrollArea_vault.setObjectName("scrollArea_vault")
        self.scrollAreaWidgetContents_vault = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_vault.setGeometry(QtCore.QRect(0, 0, 436, 530))
        self.scrollAreaWidgetContents_vault.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_vault.setAutoFillBackground(False)
        self.scrollAreaWidgetContents_vault.setStyleSheet("background-color: #34363a")
        self.scrollAreaWidgetContents_vault.setObjectName("scrollAreaWidgetContents_vault")
        self.verticalLayout_vault = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_vault)
        self.verticalLayout_vault.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_vault.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_vault.setSpacing(0)
        self.verticalLayout_vault.setObjectName("verticalLayout_vault")
        self.groupBox_logoBackground_vault = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_vault)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_logoBackground_vault.sizePolicy().hasHeightForWidth())
        self.groupBox_logoBackground_vault.setSizePolicy(sizePolicy)
        self.groupBox_logoBackground_vault.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_logoBackground_vault.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_logoBackground_vault.setStyleSheet("background-color: #454547;")
        self.groupBox_logoBackground_vault.setTitle("")
        self.groupBox_logoBackground_vault.setObjectName("groupBox")
        self.label_audit = QtWidgets.QLabel(self.groupBox_logoBackground_vault)
        self.label_audit.setGeometry(QtCore.QRect(round((MainWindow.width() - 500) / 2), round((self.groupBox_logoBackground_vault.height() - 150)/2), 500, 150))
        self.label_audit.setStyleSheet("")
        self.label_audit.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label_audit.setScaledContents(True)
        self.label_audit.setObjectName("label_audit")
        self.verticalLayout_vault.addWidget(self.groupBox_logoBackground_vault)
        
        self.groupBox_2_vault = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_vault)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2_vault.sizePolicy().hasHeightForWidth())
        self.groupBox_2_vault.setSizePolicy(sizePolicy)
        self.groupBox_2_vault.setMinimumSize(QtCore.QSize(0, 125))
        self.groupBox_2_vault.setStyleSheet("background-color: #d2c15d;")
        self.groupBox_2_vault.setTitle("")
        self.groupBox_2_vault.setObjectName("groupBox_2_vault")
        self.widget_vault = QtWidgets.QWidget(self.groupBox_2_vault)
        self.widget_vault.setGeometry(QtCore.QRect(10, 20, 800, 71))
        self.widget_vault.setStyleSheet("")
        self.widget_vault.setObjectName("widget_vault")
        self.horizontalLayout_vault = QtWidgets.QHBoxLayout(self.widget_vault)
        self.horizontalLayout_vault.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_vault.setSpacing(0)
        self.horizontalLayout_vault.setObjectName("horizontalLayout_vault")
        self.HomeBtn_vault = QtWidgets.QPushButton(self.widget_vault)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HomeBtn_vault.sizePolicy().hasHeightForWidth())      
       
        self.HomeBtn_vault.setSizePolicy(sizePolicy)
        self.HomeBtn_vault.setStyleSheet("background-color: #d2c15d;")
        self.HomeBtn_vault.setObjectName("HomeBtn_vault")
        self.HomeBtn_vault.setProperty("class", "navBarBtn")
        self.horizontalLayout_vault.addWidget(self.HomeBtn_vault)
        self.SettingsBtn_vault = QtWidgets.QPushButton(self.widget_vault)
      
        sizePolicy.setHeightForWidth(self.SettingsBtn_vault.sizePolicy().hasHeightForWidth())
        self.SettingsBtn_vault.setSizePolicy(sizePolicy)
        self.SettingsBtn_vault.setStyleSheet("")
        self.SettingsBtn_vault.setObjectName("SettingsBtn_vault")
        self.SettingsBtn_vault.setProperty("class", "navBarBtn")
        self.horizontalLayout_vault.addWidget(self.SettingsBtn_vault)
        self.AboutUsBtn_vault = QtWidgets.QPushButton(self.widget_vault)
    
        sizePolicy.setHeightForWidth(self.AboutUsBtn_vault.sizePolicy().hasHeightForWidth())
        self.AboutUsBtn_vault.setSizePolicy(sizePolicy)
        self.AboutUsBtn_vault.setStyleSheet("")
        self.AboutUsBtn_vault.setObjectName("AboutUsBtn_vault")
        self.AboutUsBtn_vault.setProperty("class", "navBarBtn")
        self.horizontalLayout_vault.addWidget(self.AboutUsBtn_vault)
        self.verticalLayout_vault.addWidget(self.groupBox_2_vault)

        self.groupBox_searchbar_vault = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_vault)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_searchbar_vault.sizePolicy().hasHeightForWidth())
        self.groupBox_searchbar_vault.setSizePolicy(sizePolicy)
        self.groupBox_searchbar_vault.setMinimumSize(QtCore.QSize(0,70))
        self.groupBox_searchbar_vault.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_searchbar_vault.setStyleSheet(""" background-color: grey; border-style: none;""")
        self.searchbar = QtWidgets.QLineEdit(self.groupBox_searchbar_vault)
        self.searchbar.setGeometry(QtCore.QRect(0,0, MainWindow.width() - 28, 70))
        self.searchbar.textChanged.connect(self.update_display)
        self.searchbar.setPlaceholderText("Search the vault")
        self.searchbar.setStyleSheet(""" background-color: rgba(255, 255, 255, 50); font-size: 30px;
        border-style: none; padding-left: 10px;
        """)
        sizePolicy.setHeightForWidth(self.searchbar.sizePolicy().hasHeightForWidth())      

        spacer_vault = QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_vault.addWidget(self.groupBox_searchbar_vault)

       

        #list of names, widgets are stored in a dictionary
        widget_names = [
            "Facebook", "Twitter", "Instagram", "Telegram", "Snapchat"
        ]
        self.widgets = []

        #Iterate the names, creating a new OnOffWidget for
        #each one, adding it to the layout and 
        #storing a reference in the 'self.widgets' dict
        for name in widget_names:
            item = OnOffWidget(name)
            self.verticalLayout_vault.addWidget(item)
            self.widgets.append(item)

         #to maintain the positions of each items inside the layout
        self.verticalLayout_vault.addItem(spacer_vault)

        self.completer_vault = QtWidgets.QCompleter(widget_names)
        self.completer_vault.setCaseSensitivity(QtCore.Qt.CaseInsensitive)        
        self.searchbar.setCompleter(self.completer_vault)
        
        self.scrollArea_vault.setWidget(self.scrollAreaWidgetContents_vault)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 18))
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
        self.label_audit.setText(_translate("MainWindow", ""))
        self.HomeBtn_vault.setText(_translate("MainWindow", "Home"))
        self.SettingsBtn_vault.setText(_translate("MainWindow", "Settings"))
        self.AboutUsBtn_vault.setText(_translate("MainWindow", "About Us"))
       
       
    def update_display(self, text):

        for widget_vault in self.widgets:
            if text.lower() in widget_vault.name.lower():
                widget_vault.show()
            else:
                widget_vault.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.styleSheet = """
        .navBarBtn {
            background:linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
            background-color: #d2c15d;
            font-size: 20px;
            font-family: Trebuchet MS;
            font-weight: bold;
            border-style: none; 
        }

        .navBarBtn:hover {
            border: 5px solid #6da4fc;
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }

        .navBarBtn:active {
            position:relative;
            top:1px;
        }

        QGroupBox {
            border-style: none;
        }

    
    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
