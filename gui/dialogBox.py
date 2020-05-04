# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 205)
        self.dialogBox = QtWidgets.QDialogButtonBox(Dialog)
        self.dialogBox.setGeometry(QtCore.QRect(30, 160, 341, 32))
        self.dialogBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.dialogBox.setObjectName("dialogBox")

        self.retranslateUi(Dialog)
        self.dialogBox.accepted.connect(Dialog.accept)
        self.dialogBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
