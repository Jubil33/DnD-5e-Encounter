from .action import action

class Party:
    playerCount=0
    playerLvl=0
    
    def __init__(self,pc,pl):
        self.playerCount=pc
        self.playerLvl=pl
    
    #calculate and return the party Capacity
    def calculateCapacity(self):
        return self.playerCount*self.playerLvl/4
    
    