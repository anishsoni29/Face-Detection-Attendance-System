import firebase_admin
from firebase_admin import credentials
from firebase import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://realtimeattendancesystem-40b3a-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')