import json  # # Import json module

from flask import Flask  # # Import Flask framework module

app = Flask(__name__)
## Define json object
data = json.load(open('dev/data/sample.json', 'r'))


@app.route("/")  ## routing to localhost:5000
def hello():
    return data['web-content'] + data['image'] + data['para']


@app.route("/next")  ## routing to localhost:5000/next
def img():
    return data['web-content'] + data['image'] + data['para']


if __name__ == "__main__":
    app.run()
