# customwidgets.py
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QSizePolicy)
from PyQt5.QtCore import (QSize)

class OnOffWidget(QWidget):

    def __init__(self, name):
        super(OnOffWidget, self).__init__()

        self.name = name

        self.lbl = QLabel(self.name)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl.sizePolicy().hasHeightForWidth())
        self.lbl.setSizePolicy(sizePolicy)
        self.lbl.setMinimumSize(QSize(0, 150))
        self.setStyleSheet("""font-size: 30px; font-family: Trebuchet MS;
        color: white;""")
   
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.lbl)
        
        self.setLayout(self.hbox)


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

    