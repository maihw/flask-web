import sqlite3
from flask import Flask, render_template, g
from flask import flash, request, session
from flask import abort, redirect, url_for

DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'maihw'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)

app.config.from_object(__name__)

def db_conn():
    '''创建与数据库连接的对象
    '''
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    '''此函数用于创建数据表，需要在flask shell 里执行
    '''
    with db_conn() as conn:
        with app.open_resource('schema.sql') as f:
            conn.cursor().executescript(f.read().decode())
        conn.commit()

@app.before_request
def before():
    '''创建数据库的连接对像，并将其赋值给g的conn属性
    '''
    g.conn = db_conn()

@app.teardown_request
def teardown(exception):
    '''关闭与数据库的连接
    '''
    g.conn.close()

@app.route('/')
def show_entries():
    '''显示所有存储在数据表中的条目
    '''
    cursor = g.conn.execute('SELECT title, text FROM entries ORDER BY id DESC')
    entries = [dict(title=row[0], text=row[1]) for row in
    cursor.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    '''添加一条博客
    '''
    if not session.get('login'):
        abort(401)
    g.conn.execute('INSERT INTO entries(title, text) VALUES (?, ?)',
    [request.form.get('title'), request.form.get('text')])
    
    g.conn.commit()
    flash('New entry has beensucessfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''用户登陆
    '''
    error = None
    if request.method == 'POST':
        if request.form.get('username') != app.config.get('USERNAME'):
            error = 'Invalid username'
        elif request.form.get('password') != app.config.get('PASSWORD'):
            error = 'Invalid password'
        else:
            session['login'] = True
            flash('you are loginned successfully!')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    '''用户登出
    '''
    session.pop('login', None)
    flash('You have logouted successfully!')
    return redirect(url_for('show_entries'))



if __name__ == '__main__':
    app.run()
