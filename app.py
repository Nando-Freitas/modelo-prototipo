# app.py
from flask import Flask, jsonify, request, render_template
from model import *
from access_model import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        accessModel = AccessModel()

        json = request.get_json()
        grade = json['grade']
        age = json['age']
        timeCollege = json['timeCollege']

        newStudent = []
        newStudent.append(grade)
        newStudent.append(age)
        newStudent.append(timeCollege)

        resposta = accessModel.predict(newStudent)

        return resposta  # serialize and use JSON headers
    else:
        return "OK", 200

if __name__ == "__main__":
    app.run()
