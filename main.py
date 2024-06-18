#!/usr/bin/env python3
from Class.Monster import Monster
from Class.action import action
from Class.Encounter import Encounter
from Class.generateEncounter import generateEncounter
import json

#def __main__():
with open('data\srd_5e_monsters.json') as datafile:
    data = json.load(datafile)

#name, meta, AC, HP, Speed, STR, DEX, CON, INT, WIS, CHA, SThrows, Skills, DmgImmunities,Senses, Lang, Challenge, Traits, Actions, LegActions,img_URl
monsters = []
for item in data:
    monsters.append(Monster(item))
   
#mon1 = Monster("asdf")

#for e in monsters:
    #(e.name, ' ', e.actions)
    #print(e.name, 'armor class:',e.ac, 'hit points:',e.hp, 'senses:',e.senses)
    #for a in e.actions:

encHolder= generateEncounter(monsters)
lowMonsters = encHolder.setChallengeRating(2)
smallMons = encHolder.setSize('Small')
neutral=encHolder.setAlignment('unaligned')

enLowMonsters=Encounter(lowMonsters)
print('lowMonsters',enLowMonsters.calculateChallenge())
#for m in lowMonsters:
    #print(m.name, 'alignment:', m.alignment, 'challenge:',m.challenge)

EnChaEvil=Encounter(smallMons)
print('chaEvil',EnChaEvil.calculateChallenge())
for m in smallMons:
    print(m.name, 'size:', m.size, 'challenge:',m.challenge)

#print(neutral)
asdf = Encounter(encHolder.filteredMonsters)
print('asdf',asdf.calculateChallenge())
for m in asdf.monsters:
    print(m.name, 'size:', m.size, 'challenge:',m.challenge)

en = Encounter(monsters)
print('total challenge Rating: ',en.calculateChallenge())

'''
    for a in e.strAction.split("</p>"):
        a=a+"</p>"
        #print(e.name, ': ', a)
        act = action(a)
        print(e.name,' ',act.name, ': ', act.body)

testData = [
    "<p><em><strong>Multiattack.</strong></em> The dragon makes three attacks: one with its bite and two with its claws. </p><p><em><strong>Bite.</strong></em> <em>Melee Weapon Attack:</em> +9 to hit, reach 10 ft., one target. <em>Hit:</em> 16 (2d10 + 5) piercing damage plus 5 (1d10) lightning damage. </p><p><em><strong>Claw.</strong></em> <em>Melee Weapon Attack:</em> +9 to hit, reach 5 ft., one target. <em>Hit:</em> 12 (2d6 + 5) slashing damage. </p><p><em><strong>Lightning Breath (Recharge 5–6).</strong></em> The dragon exhales lightning in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw, taking 55 (10d10) lightning damage on a failed save, or half as much damage on a successful one.</p>",
    "<p><em><strong>Slam.</strong></em> <em>Melee Weapon Attack:</em> +3 to hit, reach 5 ft., one target. <em>Hit:</em> 4 (1d6 + 1) bludgeoning damage.</p>",
    "<p><em><strong>Bite.</strong></em> <em>Melee Weapon Attack:</em> +0 to hit, reach 5 ft., one creature. <em>Hit:</em> 1 piercing damage.</p>"
]

i=0
for d in testData:
    for a in d.split("</p>"):
        a=a+"</p>"
        print('data: ', a)
        #print(e.name, ': ', a)
        act = action(a)
        print(i, ':| name: ', act.name, '| body: ', act.body)
        print()

    i=i+1
'''
    
#mon2 = Monster("asdf")

#print('hello!')
#print(mon1, '/n')
#print(mon2)