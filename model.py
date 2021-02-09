import json
import pandas as pd
from random import random
from random import randint
from random import choice
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class Modelo:

    def generateGrade(self):
        nota = random()*100
        return nota

    def generateAge(self):
        age = randint(18,40)
        return age

    def generateYearsCollege(self):
        yearsCollege = randint(0,12)
        return yearsCollege

    def isRisk(self, aluno):
        if int(aluno[0]) < 500 and int(aluno[1]) < 25:
            return 1
        else:
            return 0

    def isRiskTest(self, aluno):
        risk = randint(0, 1)
        return risk
