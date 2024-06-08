#!/usr/bin/env python3
from Class.Monster import Monster
import json

#def __main__():
with open('data\srd_5e_monsters.json') as datafile:
    data = json.load(datafile)

#name, meta, AC, HP, Speed, STR, DEX, CON, INT, WIS, CHA, SThrows, Skills, DmgImmunities,Senses, Lang, Challenge, Traits, Actions, LegActions,img_URl
monsters = []
for item in data:
    monsters.append(Monster(item))
   
#next idea would be to create an array of Monsters to meet this option, which would be great. 
#mon1 = Monster("asdf")
for e in monsters:
    print(e.name, ' ', e.meta, ' ', e.traits)
#mon2 = Monster("asdf")
print('hello!')
#print(mon1, '/n')
#print(mon2)