from flask import Flask
from flask import render_template_string
from flask import request
app = Flask(__name__)

log = ''

templ = """
<!DOCTYPE html>
<div>
{{ log }}
</div>
<form action="/" method="POST">
<input name="msg">
<input type="submit" value="send">
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global log
    if request.method == 'POST':
        log += request.form['msg'] + '<br>'

    return render_template_string(templ, log=log)

if __name__ == "__main__":
    app.run()
