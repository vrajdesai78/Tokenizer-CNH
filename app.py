from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Starting of Cloud Native Hackathon'

if __name__ == '__main__':
    app.run()