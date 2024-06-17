from Class.Encounter import Encounter

class generateEncounter:
    monsters=[]
    enviornment=''
    challengeRating=0
    alignment=[]
    sizeRange=['Tiny','Small','Medium','Large','Huge','Gargantuan']
    chosenSizeRange=[]
    filteredMonsters=[]

    def __init__(self, monsters):
        self.monsters=monsters
        self.filteredMonsters=monsters

    #this will refrsh the filteredMonsters list to include the parameters for filtering. 
    '''def refreshMonsterList(self):
        mons=[]
        for m in self.monsters:
            if(self.challengeRating>=m.chchallenge):
                mons.append(m)
    '''

    def setChallengeRating(self, cr):
        self.challengeRating=cr
        mons=[]
        for m in self.monsters:
            if(self.challengeRating>=m.challenge):
                mons.append(m)
        self.filteredMonsters=mons
        return mons
    


    #the list should just filter whenever an option is chosen, that is when the option should be provided

    def randomEncounter():
        asdf=0 
        #loop through the monsters

    