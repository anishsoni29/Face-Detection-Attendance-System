import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("/Users/anishsoni/Desktop/Github Clone Project/Face-Detection-Attendance-System/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://realtimeattendancesystem-40b3a-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket':'realtimeattendancesystem-40b3a.appspot.com'
})


# Importing the students' images
folderPath = '/Users/anishsoni/Desktop/Github Clone Project/Face-Detection-Attendance-System/Images'
pathList =  os.listdir(folderPath)
print(pathList)
imgList = []
studentsIds = []

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    if img is not None:
        imgList.append(img)
        studentsIds.append(os.path.splitext(path)[0])
    else:
        print(f"Failed to load image: {os.path.join(folderPath, path)}")
    
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob =  bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentsIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentsIds]
print("Encoding Complete")

file = open('EncodeFile.p', 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
