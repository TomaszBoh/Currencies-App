from flask import Flask
from flask import jsonify
from flask import render_template

#obiekt appki
app = Flask("Walutomat")

#dodajemy pierwsze routingi (adresy)
@app.route("/")

def home_page():
    return "Home Page"

@app.route("/contact")
def contact():
    return "Contact Data"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    result = a +b 
    response = {"a": a, "b": b, "sum":result}
    return jsonify(response)

@app.route("/template1")
def template1():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/price")
def price():
    return render_template('price.html')

@app.route("/variables")
@app.route("/variables/<p_abc>")
def variables(p_abc='not given'):
    p_xyz=123
    return render_template('variables.html', abc=p_abc, xyz=p_xyz)

@app.route("/person")
def person():
    person = {
        "first_name": "Jan",
        "last_name": "Winnicki",
        "age": 52,
        "adress": "Alternatywy 4"

    }
    return render_template('person.html', person=person)


if __name__ == "__main__":
    app.run()