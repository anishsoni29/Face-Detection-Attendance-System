import cv2, os
import face_recognition
import numpy as np
import pickle
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("/Users/anishsoni/Desktop/Github Clone Project/Face-Detection-Attendance-System/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://realtimeattendancesystem-40b3a-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket':'realtimeattendancesystem-40b3a.appspot.com'
})

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread("/Users/anishsoni/Desktop/Github Clone Project/Face-Detection-Attendance-System/Resources/background.png")

#Importing the mode images into a list
folderModePath = '/Users/anishsoni/Desktop/Github Clone Project/Face-Detection-Attendance-System/Resources/Modes'
modePathList =  os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# print(len(imgModeList))

#Load the encoding file
print("Loading Encoding File...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encoding File Loaded")


while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print("matches", matches)
        # print("faceDis", faceDis)

        matchIndex = np.argmin(faceDis)
        # print("Match Index", matchIndex)
        # print(studentIds[matchIndex])

        if matches[matchIndex]:
            # print("Known Face Detected")
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55+x1, 162+y1, x2-x1, y2-y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)


    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Recognition", imgBackground)
    cv2.waitKey(1)