from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def get_lianxi():
    return render_template("lianxi.html")