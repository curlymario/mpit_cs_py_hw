from flask import Flask
from flask import request
from flask import url_for
app = Flask(__name__)

log = ''

@app.route('/')
def index():
    return app.send_static_file('client2.html')

@app.route('/log')
def get_log():
    global log
    return log

@app.route('/send', methods=['POST'])
def send():
    global log
    print(request.form)
    log += request.form['msg'] + '<br>'
    return log

if __name__ == '__main__':
    app.run()
