from Class.Monster import Monster
from Class.action import action

class Encounter:
    monsters=[]
    encounterDifficulty=0
    players=[]
    #Probably include a custom dictionary within this class to help track the monsters stats and actions within them. 
    #challengeRate=0
    #size=[]

    def __init__(self, mons):
        #self.startingMonsters=mons
        self.monsters=mons
    
    #filtering the list would be hard
    
    def calculateChallenge(self):
        temp=0
        for mo in self.monsters:
            temp=temp+mo.challenge
        return temp
    
    #Will add in the rollInititive function to this class so that it will work nicely!
    

    #the question is how to add in the filter? I guess, for each filter chosen, you would need to update the array? 
    #Set the tempMons array.
    #the loop through the array, arranging this towards which appears that... 
        