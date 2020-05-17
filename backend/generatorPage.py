
import resource
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Generator(object):
    def setupUi(self, generatorWidget, homeFunc, vaultFunc, aboutUsFunc):
        self.scrollArea_genPas = QtWidgets.QScrollArea(generatorWidget)
        self.scrollArea_genPas.setGeometry(QtCore.QRect(
            0, 0, generatorWidget.width(), generatorWidget.height() - 20))
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
        self.label_genPas.setGeometry(QtCore.QRect(round((generatorWidget.width(
        ) - 500) / 2), round((self.groupBox_logoBackground_genPas.height() - 150)/2), 500, 150))
        self.label_genPas.setStyleSheet("")
        self.label_genPas.setPixmap(QtGui.QPixmap(":/images/images/ezPassLogo.PNG"))
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
        self.HomeBtn_genPas.clicked.connect(homeFunc)

        self.VaultBtn_genPas = QtWidgets.QPushButton(self.layoutWidget_genPas)
        self.VaultBtn_genPas.setSizePolicy(sizePolicy)
        self.VaultBtn_genPas.setStyleSheet("")
        self.VaultBtn_genPas.setObjectName("HomeBtn_genPas")
        self.VaultBtn_genPas.setProperty("class", "navBar_btn")
        self.VaultBtn_genPas.clicked.connect(vaultFunc)

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
        self.AboutUsBtn_genPas.clicked.connect(aboutUsFunc)
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
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

        if (self.comboBox_wordNo == ""):
            print("Please try again.")
        else:
            self.finalResult.setText(generate_password(self.btnList, int(
                self.comboBox_wordNo), self.preferenceList))
            self.resultWidget_HLayout.addWidget(self.displayText)
            self.resultWidget_HLayout.addWidget(self.finalResult)
            self.resultWidget_HLayout.addWidget(self.copyPassPhrasebtn)
            self.resultWidget_HLayout.addWidget(self.resetAllbtn)
            

            self.verticalLayout_genPas.addWidget(self.resultLayoutWidget)