import os
from flask import Flask, request
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/shiyanlou/PROJECT/flask-web/second-flask'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \ filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    