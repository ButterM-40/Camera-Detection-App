# Github: https://github.com/opencv/opencv
# Documentation: https://docs.opencv.org/

import cv2
import sys
import random

# Load image from argument
#img = cv2.imread('People.jpg', 1)
# Load some pre-trained data on face frontals from opencv (haar cascade algo)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
img = cv2.imread('People.jpg', 1)

# Make gray and wait
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale2(gray)

# draw rectangles around face
index = 0;
print(face_coordinates)
for (x, y, w, h) in face_coordinates[0]:
# Only draw if confidence is above 40
  if face_coordinates[1][index] >= 40:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 10)
  index += 1

# Show and wait
#cv2.imshow('Face Detector', img)
cv2.waitKey()

print("Code completed")
