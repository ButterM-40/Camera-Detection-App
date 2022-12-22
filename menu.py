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
        face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        body_cascade = cv2.CascadeClassifier('data/haarcascade_upperbody.xml')
        smile_cascade = cv2.CascadeClassifier('data/haarcascade_smile.xml')
        eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye_tree_eyeglasses.xml')

        # Detect Faces
        faces = eye_cascade.detectMultiScale(img, 1.1, 4)

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

        def frameDetectionList(frame):
            #SetUp Detection
            trained_face_data = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
            trained_body_data = cv2.CascadeClassifier('data/haarcascade_upperbody.xml')
            trained_smile_data = cv2.CascadeClassifier('data/haarcascade_smile.xml')
            trained_eye_data = cv2.CascadeClassifier('data/haarcascade_eye_tree_eyeglasses.xml')

            #SetUp Frame
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_gray = cv2.equalizeHist(frame_gray)
            #Detect Face
            # Detect faces
            face_coordinates = trained_face_data.detectMultiScale2(frame, 1.1, 4)
            body_coordinates = trained_body_data.detectMultiScale2(frame, 1.1, 4)
            smile_coordinates = trained_smile_data.detectMultiScale2(frame, 1.1, 4)
            eye_coordinates = trained_eye_data.detectMultiScale2(frame, 1.1, 4)

            #Detect Face
            for(x,y,w,h) in face_coordinates[0]:
                center = (x+w//2, y+h//2)
                frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
            #Detect Body
            #for(x,y,w,h) in body_coordinates[0]:
            #    center = (x+w//2, y+h//2)
            #    frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
            #Detect Smile
            #for(x,y,w,h) in smile_coordinates[0]:
            #    center = (x+w//2, y+h//2)
            #    frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
            #Detect Eyes
            for(x,y,w,h) in eye_coordinates[0]:
                center = (x+w//2, y+h//2)
                frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
            cv2.imshow('Capture - Face detection', frame)

        while True:
            ret, frame = cap.read()

            frameDetectionList(frame)

            #cv2.imshow('frame', frame)

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
