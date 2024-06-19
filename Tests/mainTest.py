from Class.Monster import Monster
from Class.action import action
from Class.Encounter import Encounter
from Class.generateEncounter import generateEncounter
import json
import unittest

#the main purpose of this is to practice some unit testing to see what can be tested within this space. 
#I'll have to wait a little bit while I do some cleaning of this space and prepare a bit for it.
class mainTest:
    monsters = []
    def __init__(self):
        with open('data\srd_5e_monsters.json') as datafile:
            data = json.load(datafile)

        for item in data:
            self.monsters.append(Monster(item))
        
        self.checkGenerateEncounters(self.monsters)

    def mainSpace(self):
        self.checkMonsters()
    
    #test monsters: doesn't test actions, traits, languages, skills
    def checkMonsters(self):
        data = {
            "name": "Adult Copper Dragon",
            "meta": "Huge dragon, chaotic good",
            "Armor Class": "18 (Natural Armor)",
            "Hit Points": "184 (16d12 + 80)",
            "Speed": "40 ft., climb 40 ft., fly 80 ft. ",
            "STR": "23",
            "STR_mod": "(+6)",
            "DEX": "12",
            "DEX_mod": "(+1)",
            "CON": "21",
            "CON_mod": "(+5)",
            "INT": "18",
            "INT_mod": "(+4)",
            "WIS": "15",
            "WIS_mod": "(+2)",
            "CHA": "17",
            "CHA_mod": "(+3)",
            "Saving Throws": "DEX +6, CON +10, WIS +7, CHA +8",
            "Skills": "Deception +8, Perception +12, Stealth +6",
            "Damage Immunities": "Acid",
            "Senses": "Blindsight 60 ft., Darkvision 120 ft.,  Passive Perception 22",
            "Languages": "Common, Draconic",
            "Challenge": "14 (11,500 XP)",
            "Traits": "<p><em><strong>Legendary Resistance (3/Day)</strong></em> If the dragon fails a saving throw, it can choose to succeed instead.</p>",
            "Actions": "<p><em><strong>Multiattack.</strong></em> The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws. </p><p><em><strong>Bite.</strong></em> <em>Melee Weapon Attack:</em> +11 to hit, reach 10 ft., one target. <em>Hit:</em> 17 (2d10 + 6) piercing damage. </p><p><em><strong>Claw.</strong></em> <em>Melee Weapon Attack:</em> +11 to hit, reach 5 ft., one target. <em>Hit:</em> 13 (2d6 + 6) slashing damage. </p><p><em><strong>Tail.</strong></em> <em>Melee Weapon Attack:</em> +11 to hit, reach 15 ft., one target. <em>Hit:</em> 15 (2d8 + 6) bludgeoning damage. </p><p><em><strong>Frightful Presence.</strong></em> Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours. </p><p><em><strong>Breath Weapons (Recharge 5–6).</strong></em> The dragon uses one of the following breath weapons. </p><p><em><strong>Acid Breath.</strong></em> The dragon exhales acid in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 54 (12d8) acid damage on a failed save, or half as much damage on a successful one. </p><p><em><strong>Slowing Breath.</strong></em> The dragon exhales gas in a 60-foot cone. Each creature in that area must succeed on a DC 18 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save.</p>",
            "Legendary Actions": "<p>The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn. </p><p><em><strong>Detect.</strong></em> The dragon makes a Wisdom (Perception) check. </p><p><em><strong>Tail Attack.</strong></em> The dragon makes a tail attack. </p><p><em><strong>Wing Attack (Costs 2 Actions).</strong></em> The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed.</p>",
            "img_url": "https://media-waterdeep.cursecdn.com/avatars/thumbnails/0/22/1000/1000/636238956325913912.jpeg"
        }
        
        mons=Monster(data)
        assert mons.name=="Adult Copper Dragon"
        assert mons.alignment=="chaotic good"
        assert mons.size=="Huge"
        assert mons.monsterType=="dragon"
        assert mons.ac==18
        assert mons.hp==184
        assert mons.challenge==14

    #test encounter. Takes in the monsters array and confirms that it returns the right value.
    def checkEncounters(self):
        encHolder= Encounter(self.monsters)
        assert encHolder.calculateChallenge()==1485.125

    def checkGenerateEncounters(self,monsters):
        encHolder= generateEncounter(monsters)
        
        challenge2=Encounter(encHolder.setChallengeRating(2))
        alignmenta=Encounter(encHolder.setAlignment("chaotic good"))
        alignmentb=Encounter(encHolder.setAlignment("lawful good"))
        sizea=Encounter(encHolder.setSize('Medium'))
        encHolder.resetFilters()
        monsList=Encounter(encHolder.monsters)
        alignmentc=Encounter(encHolder.setAlignment('unaligned'))

        assert challenge2.calculateChallenge()==136.125
        assert alignmenta.calculateChallenge()==4.0
        assert alignmentb.calculateChallenge()==8.25
        assert sizea.calculateChallenge()==6.25
        assert monsList.calculateChallenge()==1485.125
        assert alignmentc.calculateChallenge()==256.125

        #check the filter for each...

    def loadData():
        asdf=0
    
    def OldCodeInMain():
        '''
        #def __main__():
        with open('data\srd_5e_monsters.json') as datafile:
            data = json.load(datafile)

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
