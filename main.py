#!/usr/bin/env python3
from Class.Monster import Monster
from Class.action import action
from Class.Encounter import Encounter
from Class.generateEncounter import generateEncounter
from Tests.mainTest import mainTest
from Class.party import Party
import json
import random

'''
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        print('accessed hello page')
        return 'Hello, World!'

    return app


while True:
    print(random.randint(0,100))
'''
    
test = mainTest()
test.runAllTests()

def loadData():
    monsters=[]
    with open('data\srd_5e_monsters.json') as datafile:
        data = json.load(datafile)

    for item in data:
        monsters.append(Monster(item))
    return monsters
  

'''
genen=generateEncounter(monsters,Party(4,9))
asdf=genen.setChallengeRating(3)

for m in asdf:
    print(m.name,' ', m.challenge, ' ', m.experiencePoints)
'''