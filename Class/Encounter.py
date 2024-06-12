from Class.Monster import Monster
from Class.action import action

class Encounter:
    #include some parameters... What do the take for this... 
    monsters=[]
    challengeRate=0

    def __init__(self, mons):
        monsters=mons
        