from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def show_name(name):
    return 'name'

@app.route('/sum/<int:a>/<int:b>')
def sum(a, b):
    retun '{0} + {1} = {2}'.format(a, b, a+b)