from Class.Monster import Monster
from Class.action import action
from Class.Encounter import Encounter
from Class.generateEncounter import generateEncounter
#from ..Tests.mainTest import mainTest
from Class.party import Party
import json
import random

import functools

from flask import (
    Blueprint, render_template #, flash, g, redirect, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('encounter', __name__, url_prefix='/encounter')

class encounterController:
    asdf=0

    def __init__(self):
        self.monsters = self.loadData()

    @bp.route('/encounter', methods=('GET', 'POST'))
    def encounter():
        return render_template('encounter.html')
    
    def loadData():
        monsters=[]
        with open('data\srd_5e_monsters.json') as datafile:
            data = json.load(datafile)

        for item in data:
            monsters.append(Monster(item))
        return monsters
    
    