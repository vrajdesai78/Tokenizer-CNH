from flask import Flask
from flask import render_template
from firebase_admin import db, credentials, initialize_app, firestore

app = Flask(__name__)

cred = credentials.Certificate('config.json')
initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/places')
def places():
    place_details = []
    place_ref = db.collection(u'Places').stream()
    for place in place_ref:
        place_details.append(place.to_dict())
        # for key, value in place.to_dict().items():
        #     place_details[key] = value

    return render_template('places.html', places=place_details)

if __name__ == '__main__':
    app.run(debug=True)