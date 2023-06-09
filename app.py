from flask import Flask, render_template,jsonify,send_file,make_response,request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')
