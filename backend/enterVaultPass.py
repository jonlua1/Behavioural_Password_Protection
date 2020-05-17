import sys
import resource
from PyQt5 import QtWidgets, QtCore, QtGui


class vaultPassword(QtWidgets.QDialog):

    def __init__(self):
        super(vaultPassword, self).__init__()


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/lock_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        self.setWindowIcon(icon)
        self.setGeometry(QtCore.QRect(500, 400, 700, 600))
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0,0, 650, 400))
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
        self.PasLabel = QtWidgets.QLabel("Please enter vault password.")
        self.PasLabel.setMinimumHeight(100)
        self.PasLabel.setStyleSheet("""background-color: #d2c15d;
            color: black;
            border: none;
            padding-left: 20px;
            """)
        self.PasLabel.setFont(font)

        self.button_box = QtWidgets.QDialogButtonBox(self)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.setContentsMargins(0,0,0,80)
        self.button_box.setGeometry(QtCore.QRect(0, 450, 400, 60))
        self.buttonOk = self.button_box.button(QtWidgets.QDialogButtonBox.Ok)
        self.buttonOk.setText("Log in")
        self.buttonOk.setMinimumSize(250, 50)
        self.buttonCancel = self.button_box.button(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonCancel.setText("Cancel")
        self.buttonCancel.setMinimumHeight(50)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        spacerItem = QtWidgets.QSpacerItem(20, 73, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
       
        self.layout.addRow(self.PasLabel)
        self.layout.addItem(spacerItem)
        self.layout.addRow('Password : ', self.password)
 
        self.widget.setLayout(self.layout)
        self.setWindowTitle("Please enter password")
        self.setMinimumWidth(350)
