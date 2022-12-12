import json  # # Import json module

## Import Flask framework module  ## render_template module
from flask import Flask, render_template

app = Flask(__name__)
## Define json object
data = json.load(open('dev/data/sample2.json', 'r'))


@app.route("/")  ## routing to localhost:5000
def hello():
    return render_template('index.html', data=data)


@app.route("/next")
def next():
    return render_template('next.html', title=data['title'], image=data['image'], para=data['para'])


@app.route("/next/<variable_option1>")
def next_and_variable(variable_option1):
    data.update({"variable1": variable_option1})
    return render_template('next_and_variable.html',
                           title=data['title'],
                           image=data['image'],
                           para=data['para'],
                           variable1=data['variable1'])


@app.route("/next/<variable_option1>/<variable_option2>")
def next_and_2_variables(variable_option1, variable_option2):
    data.update({"variable1": variable_option1, "variable2": variable_option2})
    return render_template('next_and_2_variables.html',
                           title=data['title'],
                           image=data['image'],
                           para=data['para'],
                           variable1=data['variable1'],
                           variable2=data['variable2'])


if __name__ == "__main__":
    app.run(debug=True)
