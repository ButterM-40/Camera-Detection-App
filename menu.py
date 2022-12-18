from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi 
from PyQt5.QtGui import *
import cv2

import sys


class Main(QDialog):
    def __init__(self):
        super(Main,self).__init__()
        loadUi("mainScreen.ui",self)
        self.image_button.clicked.connect(self.goToImageSelect)
        self.camera_button.clicked.connect(self.gotoCameraSelect)
    def goToImageSelect(self):
        #imageSelect2=imageSelect()
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoCameraSelect(self):
        #print(widget.currentIndex())
        widget.setCurrentIndex(widget.currentIndex()+2)

class imageSelect(QDialog):
    def __init__(self):
        super(imageSelect,self).__init__()
        loadUi("imageSelect.ui",self)
        self.back_button.clicked.connect(self.goMain)
        self.browse_button.clicked.connect(self.browsefiles)
    def browsefiles(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Images (*.png, *.xmp, *.jpg)')
        self.browse_textbox.setText(filename[0])
    def goMain(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class cameraSelect(QDialog):
    def __init__(self):
        super(cameraSelect,self).__init__()
        loadUi("cameraSelect.ui",self)
        self.cameraButtonReady.clicked.connect(self.startCamera)
    def startCamera(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
main = Main()
imageS = imageSelect()
cameraS = cameraSelect()
widget.addWidget(main)
widget.addWidget(imageS)
widget.addWidget(cameraS)
widget.show()

#main.show()
sys.exit(app.exec_())
