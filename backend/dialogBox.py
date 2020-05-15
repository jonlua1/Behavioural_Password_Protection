# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, displayText):
        self.displayText = displayText
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 324)
 
        Dialog.setWindowOpacity(1.0)
        Dialog.setSizeGripEnabled(False)
        self.dialogBox = QtWidgets.QDialogButtonBox(Dialog)
        self.dialogBox.setGeometry(QtCore.QRect(round((Dialog.width()- 340) / 2), 210, 340, 32))
        self.dialogBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonOk = self.dialogBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.buttonOk.setText("Ok")
        self.buttonCancel = self.dialogBox.button(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonCancel.setMinimumWidth(100)
        

        self.dialogBox.setObjectName("dialogBox")
        self.label = QtWidgets.QLabel(Dialog)
        if (len(self.displayText) < 20):    
            self.label.setGeometry(QtCore.QRect(round((Dialog.width()- 450) / 2), 70, 450, 91))
        else:
            self.label.setGeometry(QtCore.QRect(round((Dialog.width()- 700) / 2), 70, 700, 91))

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        Dialog.setWindowFlags(flags)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        

        self.retranslateUi(Dialog)
        self.dialogBox.accepted.connect(Dialog.accept)
        self.dialogBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", self.displayText))

    


