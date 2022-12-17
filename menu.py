from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi 
from PyQt5.QtGui import *
 
import sys


class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        loadUi("mainScreen.ui",self)
        self.pushButton.clicked.connect(self.goToImageSelect)
        self.pushButton_2.clicked.connect(self.goToImageSelect)
    def goToImageSelect(self):
        #imageSelect2=imageSelect()
        widget.setCurrentIndex(widget.currentIndex()+1)

class imageSelect(QDialog):
    def __init__(self):
        super(imageSelect,self).__init__()
        loadUi("imageSelect.ui",self)

app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
main = Main()
imageS = imageSelect()
widget.addWidget(main)
widget.addWidget(imageS)
widget.show()

#main.show()
sys.exit(app.exec_())
