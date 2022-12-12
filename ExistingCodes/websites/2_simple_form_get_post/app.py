# https://medium.com/@mikaelagurney/add-dynamic-components-to-your-html-templates-using-form-s-flask-and-jinja-59b4169ec3e1
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/response', methods=['POST'])
def response():
    fname = request.form.get("fname")
    note = request.form.get("note")
    return render_template("index.html", name=fname, note=note)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)