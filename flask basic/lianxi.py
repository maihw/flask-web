from flask import Flask
app = Flask(__name__)

@app.route("/<username>")
def get_name(username):
    return username

@app.route('/sum/<int:a>/<int:b>')
def get_sum(a,b):
    return "{} + {} = {}".format(a,b,a+b)