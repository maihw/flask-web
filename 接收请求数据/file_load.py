from flask import request

@app.route('/upload', method=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
f.save('/var/www/uploads/uploaded_file.txt')

#你可以访问filename属性。但请记住永远不要信任这个值，
#因为这个值可以伪造。如果你想要使用客户端的文件名来在服务器上存储文件，
#把它传递到 Werkzeug 提供给你的 secure_filename() 函数

from flask import request
from werkzeug import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
