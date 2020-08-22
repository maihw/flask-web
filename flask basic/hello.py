from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/hello")
def hello_world():
    return "hello,world!"

@app.route("/user/<username>")
def show_user_profile(username):
    return "user {}".format(username)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post {}".format(post_id)

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "subpth {}".format(subpath)

@app.route("/projects/")
def projects():
    return "the project page"
#此时如果访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。
#当访问 http://127.0.0.1:5000/about 时，页面会显示 The about page ；
#但是当访问 http://127.0.0.1:5000/about/ 时，页面就会报错 Not Found 。
@app.route("/about")
def about():
    return "the about page"

#默认情况下，路由只会响应 GET 请求，
#但是能够通过给route() 装饰器提供 methods 参数来改变。
@app.route("/login", method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()  # 如果是 POST 方法就执行登录操作
    else:
        show_the_login_form()  # 如果是 GET 方法就展示登录表单