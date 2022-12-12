import json  # # Import json module

## Import Flask framework module  ## render_template module
from flask import Flask, render_template

app = Flask(__name__)
## Define json object
data = json.load(open('dev/data/list_items.json', 'r'))


@app.route("/")  ## routing to localhost:5000
def hello():
    return render_template('search_box_designs.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
