from ctypes import addressof
from flask import Flask
from flask import render_template, request, redirect, url_for
import pyrebase
from firebase_admin import credentials, firestore, initialize_app
from twilio.rest import Client


app = Flask(__name__)

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
cred = credentials.Certificate('config.json')
initialize_app(cred)
db = firestore.client()
userId = ""
account_sid = "AC02428c9c7fb839e5cb4f31e3e9d2acb4"
auth_token = "790b6caf692569d1cccec7b35d63e3f0"
client = Client(account_sid, auth_token)
places_ref = db.collection(u'Places')
users_ref = db.collection(u'Users')
bookings_ref = db.collection(u'BookingDetails')

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/places/<category>')
def places(category):
    place_details = []
    pl = places_ref.where(u'Category', u'==', category).stream()
    for place in pl:
        place_details.append(place.to_dict())
    return render_template('show_places.html', places=place_details)

@app.route('/booking/<email>', methods=['GET', 'POST'])
def booking(email):
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        contact_number = request.form['contact_number']
        pl = places_ref.where(u'Email', u'==', email).stream()
        name=""
        address=""
        for place in pl:
            place_details = place.to_dict()
            name = place_details['Name']
            address = place_details['address']
        bookings_ref.add({
            u'Business_email': email,
            u'Place_name': name,
            u'Timing': date + " at " + time,
            u'UserId': userId,
            u'address': address,
            u'Contact Number': contact_number
        })
        client.messages.create(
         from_='whatsapp:+14155238886',
         body=f"Your appointment for {name} on {date} at {time} has been booked.",
         to='whatsapp:+919099735209'
        )
        return redirect(url_for('home'))
    return render_template('bookSlot.html', email=email)

@app.route('/show_bookings')
def showBookings():
    bookings = []
    bk = bookings_ref.where(u'UserId', u'==', userId).stream()
    for booking in bk:
        bookings.append(booking.to_dict())
    return render_template('showBookings.html', bookings=bookings)

@app.route('/login', methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth.sign_in_with_email_and_password(email, password)
        global userId
        userId = user['localId']
        print("User logged in successfully")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def userRegister():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        contact_number = request.form['contact_number']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            global userId
            userId = user_id
            users_ref.document(user_id).set({
                'Name': name,
                'Email': email,
                'Contact Number': contact_number
            })
            print("User created successfully")
            return redirect(url_for('home'))
        return render_template('signup.html')
    return render_template('signup.html')

@app.route('/b_login', methods=['GET', 'POST'])
def b_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth.sign_in_with_email_and_password(email, password)
        print("User logged in successfully")
        return redirect(url_for('home'))
    return render_template('b_login.html')

@app.route('/b_signup', methods=['GET', 'POST'])
def b_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        firm_category= request.form['firm']
        address = request.form['address']
        open_time = request.form['open_time']
        close_time = request.form['close_time']
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']
        users_ref.document(user_id).set({
            'Name': name,
            'Email': email,
            'Password': password,
            'Category': firm_category,
            'address': address,
            'open': open_time,
            'close': close_time
        })
        print("Place created successfully")
        return redirect(url_for('home'))
    return render_template('b_signup.html')

if __name__ == '__main__':
    app.run(debug=True)