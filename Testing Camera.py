import cv2

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
    #face_coordinates = trained_face_data.detectMultiScale2(frame, 1.1, 4)
    face_coordinates = trained_body_data.detectMultiScale2(frame, 1.1, 4)
    #face_coordinates = trained_smile_data.detectMultiScale2(frame, 1.1, 4)
    #face_coordinates = trained_eye_data.detectMultiScale2(frame, 1.1, 4)

    for(x,y,w,h) in face_coordinates[0]:
        center = (x+w//2, y+h//2)
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
        #frame = cv2.rectangle(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 2)
    cv2.imshow('Capture - Face detection', frame)

while True:
    ret, frame = cap.read()

    frameDetectionList(frame)

    #cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()