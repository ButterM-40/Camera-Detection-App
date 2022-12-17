from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi 
from PyQt5.QtGui import *
 
import sys


class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        loadUi("mainScreen.ui",self)

class imageSelect(QDialog):
    def __init__(self):
        super(imageSelect,self).__init__()
        loadUi("imageSelect.ui",self)

def window():
    app = QApplication(sys.argv)
    win = imageSelect()
    win.show()
    sys.exit(app.exec_())
    

window()