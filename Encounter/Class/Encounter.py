from .Monster import Monster
from .action import action
from .party import Party
import json

class Encounter:
    monsters=[]
    encounterDifficulty=0
    party=Party(0,0)
    #Probably include a custom dictionary within this class to help track the monsters stats and actions within them. 
    #challengeRate=0
    #size=[]

    def __init__(self, mons):
        #self.startingMonsters=mons
        self.monsters=mons
        self.party=Party(0,0)
        self.encounterDifficulty=0

    def setParty(self,party):
        self.party=party

    #returns the total challenge for the encounter.   
    def calculateMonsterChallenge(self):
        temp=0
        if self.monsters:
            for mo in self.monsters:
                temp=temp+mo.challenge
        return temp
    
    def calculateRating(self):
        playerChallenge=self.party.calculateCapacity()
        monsChallenge=self.calculateMonsterChallenge()
        return playerChallenge-monsChallenge
    
    def __str__(self) -> str:
        sti = 'Monsters: '
        for m in self.monsters:
            sti=sti+m.name+ ' ' + str(m.challenge) + ' ' #+' '+str(m.alignment)+' '
        return sti
    
    #creates a json object of the encounter code.
    def encJson(self):
        monsjson = []
        for m in self.monsters:  
            #add monster dictionary to monster list          
            monsjson.append(m.monsterDict)

        #takes in monster list and translates it to json
        json_result_default = json.dumps(monsjson, default=lambda x: list(x) if isinstance(x, tuple) else str(x), indent=2)
        return json_result_default

    #Will add in the rollInititive function to this class so that it will work nicely!

    #the question is how to add in the filter? I guess, for each filter chosen, you would need to update the array? 
    #Set the tempMons array.
    #the loop through the array, arranging this towards which appears that... 
        