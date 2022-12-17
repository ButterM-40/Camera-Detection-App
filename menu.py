from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import * 
import sys


class MyWindow(QMainWindow):
    x = 0
    y = 0
    z = 0 
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()  

    def applied_clicked(self):
        self.label1.setText(str(self.x))
        self.x+= 1
        self.update()
    def declined_clicked(self):
        self.label2.setText(str(self.y))
        self.y+= 1
        self.update()
    def accepted_clicked(self):
        self.label3.setText(str(self.z))
        self.z+= 1
        self.update()

    def initUI(self):
        #widget = QtWidgets()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Application Checker")

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText(str(self.x))
        self.label1.setGeometry(50, 50, 50, 50)
        self.label1.setStyleSheet("border: 1px solid black;")
        self.label1.setFont(QFont('Arial', 10))
        self.label1.move(200,0)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText(str(self.y))
        self.label2.setGeometry(50, 50, 50, 50)
        self.label2.setStyleSheet("border: 1px solid black;")
        self.label2.setFont(QFont('Arial', 10))
        self.label2.move(200, 40)

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setText(str(self.z))
        self.label3.setGeometry(50, 50, 50, 50)
        self.label3.setStyleSheet("border: 1px solid black;")
        self.label3.setFont(QFont('Arial', 10))
        self.label3.move(200, 80)
        
        #Creating the Buttons Variables
        self.b1 = QtWidgets.QPushButton(self)
        self.b2 = QtWidgets.QPushButton(self)
        self.b3 = QtWidgets.QPushButton(self)

        #Setting Buttons Size
        self.b1.setGeometry(200, 200, 120, 40)
        self.b2.setGeometry(200, 200, 120, 40)
        self.b3.setGeometry(200, 200, 120, 40)

        #Button Location, mostly just 3 buttons for different actions.
        #Setting their Test, Function and Location
        self.b1.setText("Internship Applied")
        self.b1.clicked.connect(self.applied_clicked)
        self.b1.move(0, 0)
        
        self.b2.setText("Internship Declined")
        self.b2.clicked.connect(self.declined_clicked)
        self.b2.move(0, 40)
        
        self.b3.setText("Internship Accepted")
        self.b3.clicked.connect(self.accepted_clicked)
        self.b3.move(0, 80)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()