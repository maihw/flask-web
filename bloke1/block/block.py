import sqlite3
from flask import (Flask, render_template, g,
flash, request, session, abort, redirect, url_for)

DATABASE = '/tmp/block.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def db_conn():
    '''创建与数据库连接的对象
    '''
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run