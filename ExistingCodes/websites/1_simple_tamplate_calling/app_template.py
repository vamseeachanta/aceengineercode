# Reference: https://pythonspot.com/flask-with-static-html-files/
from flask import Flask, render_template

app = Flask(__name__)

# Template Rendering Example
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name) #</string:page_name>

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)