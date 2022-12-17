from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi 
from PyQt5.QtGui import *
 
import sys


class MyWindow(QDialog):
    def __init__(self):
        super(MyWindow,self).__init__()
        loadUi("mainScreen.ui",self)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()