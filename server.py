from flask import Flask, request, Response, jsonify
from werkzeug.utils import secure_filename
import json, os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jps', 'jpeg', 'gif'}


def allowed_file(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def hello_world():
    re = request.args.getlist('p')
    return str(re)


@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname', default='little apple'))
    return 'welcome'


@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)


@app.route('/add2', methods=['POST'])
def add2():
    result = {'sum': request.json['a'] + request.json['b']}
    # res = Response(json.dumps(result), mimetype='application/json')
    # res.headers.add('Server', 'python flask')
    return jsonify(result)


@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'info is ' + request.form.get('info', '')+'.success'
    else:
        return 'failed'


if __name__ == '__main__':
    app.run(port=6000)
