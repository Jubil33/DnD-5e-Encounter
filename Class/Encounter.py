from Class.Monster import Monster
from Class.action import action

class Encounter:
    #include some parameters... What do the take for this... 
    monsters=[]
    challengeRate=0
    size=[]

    def __init__(self, mons):
        #self.startingMonsters=mons
        self.monsters=mons
    
    #filtering the list would be hard
    #take the filter that is available within this, then return it?
    def updateMonsterList(self):
        tempMons=[]
    
    def calculateChallenge(self):
        temp=0
        for mo in self.monsters:
            temp=temp+mo.challenge
        return temp
    #Will add in the rollInititive function to this class so that it will work nicely!
    

    #the question is how to add in the filter? I guess, for each filter chosen, you would need to update the array? 
    #Set the tempMons array.
    #the loop through the array, arranging this towards which appears that... 
        