from flask import request
#全局变量request
with app.test_request_context('/hello', method='POST'):
    #test_request_context()上下文管理器
    assert request.path == '/hello'
    assert request.method == 'POST'

from flask import request

with app.request_context(environ):
    assert request.method == 'POST'