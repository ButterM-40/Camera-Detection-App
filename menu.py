from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi 
from PyQt5.QtGui import *
import cv2
#import matplotlib.pyplot as plt

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
        self.imageButtonReady.clicked.connect(self.manipulateImage)
    def browsefiles(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Images (*.png, *.xmp, *.jpg)')
        self.browse_textbox.setText(filename[0])
        
    def manipulateImage(self):
        img = cv2.imread(self.browse_textbox.text(), 1)
        #cv2.imshow('Face Detector', img)
        #plt.imshow(img)
        #load cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Convert to grayscale
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect Faces
        faces = face_cascade.detectMultiScale(img, 1.1, 4)

        # Draw rectangle around faces
        for(x,y,w,h) in faces: 
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

        # display output
        cv2.imshow('Face Detector', img)
        cv2.waitKey()

            
    def goMain(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

class cameraSelect(QDialog):
    def __init__(self):
        super(cameraSelect,self).__init__()
        loadUi("cameraSelect.ui",self)
        self.cameraButtonReady.clicked.connect(self.startCamera)
        self.back_button.clicked.connect(self.goMain)
    def startCamera(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    def goMain(self):
        widget.setCurrentIndex(widget.currentIndex()-2)


#Main
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
