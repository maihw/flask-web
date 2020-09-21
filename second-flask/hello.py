from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello,World!'

@app.route('/tujun')
def tujun():
    return 'i love you'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post{}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath{}'.format(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
