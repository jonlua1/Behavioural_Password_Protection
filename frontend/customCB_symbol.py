#customCB.py
from PyQt5.QtWidgets import (QComboBox, QGroupBox, QSizePolicy)
from PyQt5.QtCore import (QSize)

class customComboBox_symbol(QComboBox):
    def __init__(self):
        super(customComboBox_symbol, self).__init__()

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(170, 60))
        self.setMaximumSize(QSize(250,70))
        
        self.setEnabled(True)
        self.setObjectName("comboBox_Number_2_genPas")
        self.styleSheet = """
            background-color: #d2c15d;
            color: #34363a;
            padding-left: 20px;
            font-size: 20px;
            """
        self.setStyleSheet(self.styleSheet)
        self.addItem(" ")
        self.addItem("0")
        self.addItem("1")
        self.addItem("2")
        self.addItem("3")
        self.addItem("4")
        self.addItem("5")
        self.addItem("6")
        self.addItem("7")
        self.addItem("8")
        self.addItem("9")
        self.addItem("!")
        self.addItem("@")
        self.addItem("#")
        self.addItem("$")
        self.addItem("%")
        self.addItem("^")
        self.addItem("&")
        self.addItem("*")
        

