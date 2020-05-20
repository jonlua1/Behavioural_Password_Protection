##############################################################
# This is a custom combo box that gets called when user use the
# password generator. It allows user to choose between A to Z
# and even empty string while customising his passphrase.
###############################################################

from PyQt5.QtWidgets import (QComboBox, QGroupBox, QSizePolicy)
from PyQt5.QtCore import (QSize)

class customComboBox(QComboBox):
    def __init__(self):
        super(customComboBox, self).__init__()

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
        self.addItem("a")
        self.addItem("b")
        self.addItem("c")
        self.addItem("d")
        self.addItem("e")
        self.addItem("f")
        self.addItem("g")
        self.addItem("h")
        self.addItem("i")
        self.addItem("j")
        self.addItem("k")
        self.addItem("l")
        self.addItem("m")
        self.addItem("n")
        self.addItem("o")
        self.addItem("p")
        self.addItem("q")
        self.addItem("r")
        self.addItem("s")
        self.addItem("t")
        self.addItem("u")
        self.addItem("v")
        self.addItem("w")
        self.addItem("x")
        self.addItem("y")
        self.addItem("z")
        
