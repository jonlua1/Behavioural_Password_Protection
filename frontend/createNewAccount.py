import sys
import resource
from PyQt5 import QtWidgets, QtCore, QtGui


class createAccountForm(QtWidgets.QDialog):

    def __init__(self):
        super(createAccountForm, self).__init__()


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":images/images/lock_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.setWindowIcon(icon)
        self.setGeometry(QtCore.QRect(500, 400, 700, 600))
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0,0, 650, 550))
        self.widget.setFont(font)

        self.layout = QtWidgets.QFormLayout(self.widget)
        self.layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setMinimumHeight(60)
        self.password.setStyleSheet("""background-color: #d2c15d;
            color: black;
            border: none;
            padding-left: 20px;
            """)
        self.website = QtWidgets.QLineEdit()
        self.website.setMinimumHeight(60)
        self.website.setStyleSheet("""background-color: #d2c15d;
            color: black;
            border: none;
            padding-left: 20px;
            """)
        self.username = QtWidgets.QLineEdit()
        self.username.setMinimumHeight(60)
        self.username.setStyleSheet("""background-color: #d2c15d;
            color: black;
            border: none;
            padding-left: 20px;
            """)

    

        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.setContentsMargins(0,0,0,80)
        self.buttonOk = self.button_box.button(QtWidgets.QDialogButtonBox.Ok)
        self.buttonOk.setText("Create Account")
        self.buttonOk.setMinimumSize(250, 50)
        self.buttonCancel = self.button_box.button(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonCancel.setText("Cancel")
        self.buttonCancel.setMinimumHeight(50)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        spacerItem = QtWidgets.QSpacerItem(20, 73, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        spacerItem1 = QtWidgets.QSpacerItem(20, 73, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.layout.addRow('Website   : ', self.website)
        self.layout.addItem(spacerItem)
        self.layout.addRow('User name : ', self.username)
        self.layout.addItem(spacerItem1)
        self.layout.addRow('Password  : ', self.password)
        self.layout.addItem(spacerItem2)
        self.layout.addWidget(self.button_box)


        self.widget.setLayout(self.layout)
        self.setWindowTitle("Add New Account")
        self.setMinimumWidth(350)
