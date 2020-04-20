from flask import Flask, render_template

app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>JHJ Project</h1><p>Comming Soon</p><p>TEST1</p>'''

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')
