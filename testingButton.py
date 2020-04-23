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
        self.groupBox.setGeometry(QtCore.QRect(0, round(MainWindow.height() * 0.2), MainWindow.width(), round(MainWindow.height() * 0.8)))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
 
        self.pbHeight = round(self.groupBox.height() * 0.28)
        self.pbWidth = self.groupBox.width() - 100;

        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        #self.toolButton.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), 10, self.pbWidth, self.pbHeight))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setStyleSheet("")
        self.toolButton.setText("Random Text")
        self.toolButton.setObjectName("pushButton")

        self.btn = QtWidgets.QWidget(self.groupBox)
      
        self.btn.enterEvent(QtGui.QEnterEvent(self.btn.setStyleSheet("background-color: #34363a;")))
        self.btn.setGeometry(QtCore.QRect( round((MainWindow.width() - self.pbWidth) / 2), 10, self.pbWidth, self.pbHeight))

        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 801, 91))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(174, 19, 441, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/ezPassLogo.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(-6, 90, 801, 31))
        self.label_14.setStyleSheet("")
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
        self.label_14.setText(_translate("MainWindow", "Welcome, what would you like to do?"))

    def mousePressEvent(self, event):
        print("test 1")
        QtWidgets.QWidget.mouse


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
            background:linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
            background-color:#476e9e;
        }
        QPushButton:active {
            position:relative;
            top:1px;
        }

        QLabel {
           background-color: transparent;
        }

        .btn-style {
           background-color: transparent;
        }

        QHBoxLayout {
           background-color: #ffffff;
        }
    """
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(MainWindow.styleSheet)
    sys.exit(app.exec_())
