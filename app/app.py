from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask! Its Updated to new jag'

# app.run(port=8005)