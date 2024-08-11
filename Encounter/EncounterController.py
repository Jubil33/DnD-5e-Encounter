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
    Blueprint, render_template, request, session #, flash, g, redirect, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('encounter', __name__, url_prefix='/')
encountersArr=[]

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

#function that handles recommending encounters. takes in data from request form and sets the filters for the encounter
def handleRecEncs(foam):
    recEnc = generateEncounter(monsters)
    recEnc.resetFilters()
    for f in foam:
        #print(f)
        asdf = f.replace("\"","").split("},{")
        #print("asdf",asdf)
        for s in asdf:
            s=s.replace("[","").replace("{","").replace("}","").replace("]","")
            #print(s)
            key=s[s.index("key")+4:s.index(",")]
            value=s[s.index("value")+6 :]
            #print("key:",key, value)
            if(key=="size"):
                val = value.split("|")
                for v in val:
                    recEnc.setSize(v)
                    #print("size: ",v)
                #print("size,", key, value)
                
            elif(key=="alignment"):
                val = value.split("|")
                for v in val:
                    recEnc.setAlignment(v)
                #print("alignment,", key, value)
            elif(key=="chalRate"):
                val = value.split("|")
                for v in val:
                    if v != "":
                        recEnc.setChallengeRating(v)
                #for v in val:
                #print("chalRate",key,value)
            elif(key=="pCount" and "none" not in value):
                #print(value)
                val = value.replace("|","")
                recEnc.party.playerCount=int(val)
            elif(key=="pLevel" and "none" not in value):
                #print(value)
                val = value.replace("|","")
                recEnc.party.playerLvl=int(val)
            else:
                print("key:",key, "value:",value)

    return recEnc.recommendEncounters(10)

@bp.route("/suggestFightEncounters", methods=['POST'])
def suggestFightEncounter():
    #print("got here")
    #for r in request.form:
    #    print('print req', r)
    #encountersArr.clear()
    bean = ""
    encs = handleRecEncs(request.form)
    jsonEncs = ""
    
    if encs:
        i =0
        for e in encs:
            #print(str(e))
            #encountersArr.append(e)
            jsonEncs = jsonEncs + '{id = ' + i + ', ' + e.encJson() + '}'
            bean = bean + '<div id="enc">' + str(e) + '</div>'
            i+=1
    else:
        bean = '<div id="enc"> no monsters fit desccription </div>'
    
    #this is where the function is throwing an error. I need to convert the array to json... 
    session['combatEncounters'] = jsonEncs
    return bean
#load in the request

#if(request.method == "POST"):
#    asdf=0

@bp.route('/uniqueEncounter/<variable>', methods=['GET'])
def uniqueEncounter(variable):
    #print(variable)
    s = ""
    try: 
        encs=session['combatEncounters']
    except:
        suggestFightEncounter()
        encs=session['combatEncounters']

    #take in the encounter 
    #for x in encs:
    s = "<div >aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa </div>" 
    print(encs)
    #print(s)
    return render_template('Encounter/uniqueEncounter.html',variable = variable, data = s )