import json  # # Import json module

## Import Flask framework module  ## render_template module
from flask import Flask, render_template

app = Flask(__name__)
## Define json object
data = json.load(open('dev/data/sample.json', 'r'))


@app.route("/")  ## routing to localhost:5000
def hello():
    return render_template('index.html', data=data)


@app.route("/next")  ## routing to localhost:5000/next
def img():
    return render_template('next.html', title=data['title'], image=data['image'], para=data['para'])


if __name__ == "__main__":
    app.run()
