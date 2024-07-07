#!/usr/bin/env python3
from .Class.Monster import Monster
from .Class.action import action
from .Class.Encounter import Encounter
from .Class.generateEncounter import generateEncounter
#from ..Tests.mainTest import mainTest
from .Class.party import Party
import json
import random

import functools

from flask import (
    Blueprint, render_template #, flash, g, redirect, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('encounter', __name__, url_prefix='/')


@bp.route('/encounter', methods=('GET', 'POST'))
def encounter():
    #print('navigating to encounter')
    return render_template('Encounter/Encounter.html')

def loadData():
    monsters=[]
    with open('data\srd_5e_monsters.json') as datafile:
        data = json.load(datafile)

    for item in data:
        monsters.append(Monster(item))
    return monsters

monsters = loadData()

@bp.route("/suggestFightEncounters", methods=['POST'])
def suggestFightEncounter():
    print('routed to suggest fight encounters')
    bean = ""
    recEnc = generateEncounter(monsters)
    encs = recEnc.recommendEncounters(10)
    for e in encs:
        bean = bean + '<div id="enc">' + str(e) + '</div>'
    return bean

#load in the request

#if(request.method == "POST"):
#    asdf=0

