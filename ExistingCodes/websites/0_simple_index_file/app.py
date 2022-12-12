# Reference: https://pythonspot.com/flask-with-static-html-files/
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vamsee'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)