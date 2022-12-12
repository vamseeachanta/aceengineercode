import json  # # Import json module

from flask import Flask  # # Import Flask framework module

app = Flask(__name__)
## Define json object
data = json.load(open('data\sample.json', 'r'))


@app.route("/")
def hello():
    return data['web-content']


if __name__ == "__main__":
    app.run()
