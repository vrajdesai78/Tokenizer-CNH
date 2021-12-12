import pyrebase
from firebase_admin import credentials, firestore, initialize_app

firebaseConfig = {
  "apiKey": "AIzaSyC4eW5vu9OGGOWhcrHpL85luyukeJBXD_A",
  "authDomain": "starry-acre-243615.firebaseapp.com",
  "databaseURL": "https://starry-acre-243615.firebaseio.com",
  "projectId": "starry-acre-243615",
  "storageBucket": "starry-acre-243615.appspot.com",
  "messagingSenderId": "505051276034",
  "appId": "1:505051276034:web:351104ecc519de344b981b"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

user = auth.sign_in_with_email_and_password("helloworld1@gmail.com", "123456")
print(auth.get_account_info(user['idToken']).get('users')[0].get('localId'))
print(auth.get_account_info(user['idToken']))

