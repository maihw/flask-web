from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

@app.route('/maihw/')
def maihw():
    return "i love you"

@app.errorhandler(401)
def page_not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['x-Something'] = 'A value'
    return resp