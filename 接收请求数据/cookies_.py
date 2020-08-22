#读取cookies
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    #这里引用cookies字典的键值对是使用cookies.get(key)
    #而不是cookies[key],这是防止该字典不存在时报错“keyerror"


#存储cookies:
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
