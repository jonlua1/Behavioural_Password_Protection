# customwidgets.py
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QSizePolicy, QGroupBox, QPushButton, QApplication)
from PyQt5.QtCore import (QSize, Qt, pyqtSlot)
from PyQt5.QtGui import (QClipboard)



class customGroupBox(QGroupBox):

    def __init__(self, name, uname, password):
        super(customGroupBox, self).__init__()

        self.name = name
        self.uname = uname
        self.password = password

        self.styleSheet = """ 
        QPushButton {
            font-size: 30px; 
            font-family: Trebuchet MS;
            color: white; 
            border-style: none;
        }

        QPushButton:hover { 
            color: red; 
        }  
       
        """

        self.setContentsMargins(0, 0, 0 , 0)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 200))
        self.setStyleSheet("""background-color: rgb(0, 0, 0);
        border: 5px solid white; margin: 10px; margin-left: 30px; margin-right: 30px; 
        border-radius: 50px""")

        self.btns_vault = QHBoxLayout(self)
        self.btns_vault.setSpacing(0)
        self.lbl = QLabel(self.name)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setSizePolicy(sizePolicy)
        self.lbl.setMinimumSize(QSize(0, 150))
        self.lbl.setStyleSheet("""font-size: 30px; font-family: Trebuchet MS;
        color: white; border-style: none;""")
        self.btns_vault.addWidget(self.lbl)
        self.userName = QLabel(self.uname)
        self.userName.setAlignment(Qt.AlignCenter)
        self.userName.setSizePolicy(sizePolicy)
        self.userName.setMinimumSize(QSize(0,150))
        self.userName.setStyleSheet("""font-size: 30px; font-family: Trebuchet MS;
        color: white; border-style: none;""")
        self.btns_vault.addWidget(self.userName)
       

        self.qclip = QApplication.clipboard()

    def show(self):
        """
        Show this widget, and all child widgets.
        """
        for w in [self, self.lbl]:
            w.setVisible(True)

    def hide(self):
        """
        Hide this widget, and all child widgets.
        """
        for w in [self, self.lbl]:
            w.setVisible(False)

    def delete(self):
        """
        delete this widget, and all child widgets.
        """
        for w in [self, self.lbl]:
            w.setVisible(False)

    # call mainwindow fucntion when view button is clicked
    # so that mainwindow receives the username, password and website
    # of this particular object
    def viewDetails(self, function):
        """
        calling function from MainWindow 
        """
        self.viewBtn = QPushButton("View")
        self.viewBtn.setStyleSheet(self.styleSheet)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.viewBtn.setSizePolicy(sizePolicy)
        self.viewBtn.setMinimumSize(QSize(0, 150))
        self.viewBtn.clicked.connect(lambda: function(self.password, self.userName, self.name))
        self.btns_vault.addWidget(self.viewBtn)

    @pyqtSlot()
    def copyText(self):
        self.qclip.setText(self.pwd.text())
        

    