# https://medium.com/@mikaelagurney/add-dynamic-components-to-your-html-templates-using-form-s-flask-and-jinja-59b4169ec3e1
# https://stackoverflow.com/questions/19086737/how-do-i-auto-submit-a-dropdown-when-a-value-is-selected-other-than-the-first-va
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html", vars=False)

@app.route('/response', methods=['POST'])
def response():
    FieldName = request.form.get("FieldName")
    vars = get_data_from_pkl(FieldName)
    return render_template("index.html", vars=vars)

def get_data_from_css(filename):
    import json
    import os
    filename = os.path.join(os.getcwd(), 'data', filename + '.css')
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            data = json.loads(fp)
    else:
        data = False

    return data


def get_data_from_json(filename):
    import json
    import os
    filename = os.path.join(os.getcwd(), 'data', filename + '.json')
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            data = json.loads(fp)
    else:
        data = False

    return data

def get_data_from_pkl(filename):
    import os
    import pickle
    filename = os.path.join(os.getcwd(), 'data', filename + '.pkl')
    if os.path.isfile(filename):
        with open(filename, 'rb') as fp:
            data = pickle.load(fp)
    else:
        data = False

    return data

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)