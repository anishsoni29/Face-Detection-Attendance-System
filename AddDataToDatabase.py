import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/Users/anishsoni/Desktop/Github Clone Project/Face-Detection-Attendance-System/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://realtimeattendancesystem-40b3a-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')

data = {
    "12345":
        {
            "Name": "Anish Soni",
            "Major": "Computer Science",
            "Year": "2021",
            "Roll no:": "21/189",
            "Total Attendance": "6",
            "last_attendace_time" : "19/09/2023 12:00:00"
            },

        "richard":
        {
            "Name": " Richard Branson",
            "Major": "Aviation",
            "Year": "2021",
            "Roll no:": "21/188",
            "Total Attendance": "8",
            "last_attendace_time" : "19/09/2023 12:00:00"
            },

            "steve":
        {
            "Name": "Steve Jobs",
            "Major": "Electronics & IT",
            "Year": "2021",
            "Roll no:": "21/190",
            "Total Attendance": "2",
            "last_attendace_time" : "19/09/2023 12:00:00"
            },
            "12345":
        {
            "Name": "Elon Musk",
            "Major": "Rocket Science",
            "Year": "2021",
            "Roll no:": "21/192",
            "Total Attendance": "1",
            "last_attendace_time" : "19/09/2023 12:00:00"
            }
            
        }


for key,value in data.items():
    ref.child(key).set(value)