from flask import Flask
from flask import render_template, request, redirect, url_for
import pyrebase

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

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/places')
def places():
    place_details = []
    place_ref = db.collection(u'Places').stream()
    for place in place_ref:
        place_details.append(place.to_dict())

    return render_template('places.html', places=place_details)

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/login', methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = auth.sign_in_with_email_and_password(email, password)
        print("User logged in successfully")
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def userRegister():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            auth.create_user_with_email_and_password(email, password)
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
        

    return render_template('b_signup.html')
if __name__ == '__main__':
    app.run(debug=True)