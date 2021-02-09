import json
import pandas as pd
from model import *
from random import random
from random import randint
from random import choice
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class AccessModel:

    def createStudentTraining(self, student):
        modelo = Modelo()
        for i in range(16000):
            aluno = []
            nota = modelo.generateGrade()
            aluno.append(nota)
            age = modelo.generateAge()
            aluno.append(age)
            timeCollege = modelo.generateYearsCollege()
            aluno.append(timeCollege)
            risk = modelo.isRisk(aluno)
            aluno.append(risk)
            student.append(aluno)
        return student

    def createStudentTest(self, student):
        modelo = Modelo()
        for i in range(4000):
            aluno = []
            nota = modelo.generateGrade()
            aluno.append(nota)
            age = modelo.generateAge()
            aluno.append(age)
            timeCollege = modelo.generateYearsCollege()
            aluno.append(timeCollege)
            risk = modelo.isRiskTest(aluno)
            aluno.append(risk)
            student.append(aluno)
        return student

    def executeModel(self):
        student = []
        modelo = Modelo()
        accessModel = AccessModel()
        students = accessModel.createStudentTraining(student)
        students = accessModel.createStudentTest(student)
        return students

    def predict(self, newStudent):
        accessModel = AccessModel()
        students = accessModel.executeModel()
        df = pd.DataFrame(students)
        x_train, x_test, y_train, y_test = train_test_split(df.drop([3],axis='columns'),df[3],test_size=0.2)
        model = RandomForestClassifier(n_estimators=30)
        model.fit(x_train, y_train)
        if str(model.predict([newStudent])) == "[1]":
            saida = {"risco": "o aluno representa um risco para a sua instituição.", "precisao": "com uma precisão de " + str(model.score(x_test,y_test)) + " %."}
            resposta = json.dumps(saida, indent=4, separators=(", ", " : "), ensure_ascii=False)
            return resposta
        else:
            saida = {"risco": "o aluno não representa um risco para a sua instituição.", "precisao": "com uma precisão de " + str(model.score(x_test,y_test)) + " %."}
            resposta = json.dumps(saida, indent=4, separators=(", ", " : "), ensure_ascii=False)
            return resposta
