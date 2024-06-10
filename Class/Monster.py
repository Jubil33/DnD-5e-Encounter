from Class.action import action
import math
# Monster class:
# this class is defined as a monster it will include a couple of fields such as stat and monster
#Fields: Name, meta, AC, HP Speed, STR
class Monster:
    name=""
    alignment=""
    meta=""
    ac=""
    hp=""
    speed=""
    strength=0
    dexterity=0
    constitution=0
    intelligence=0
    wisdom=0
    charisma=0
    savingThrows=""
    damageImmunities=""
    skills=""
    senses=""
    languages=""
    traits=""
    strAction=""
    actions=[]
    strLegendaryActions=""
    legendaryActions=[]
    img=""
    challenge=""
    experiencePoints=""


    #initialize monster, input a monster dictionary and loop through it's items setting the key and value for each of them
    def __init__(self,monsterDict):
        for key,value in monsterDict.items():
            if(key=='name'):
                self.name=value
            elif(key=='meta'):
                self.meta=value
                self.alignment=value.split(',')[1] #get/set the alignment
            elif(key=='Armor Class'):
                self.ac=value
            elif(key=='Hit Points'):
                self.hp=value
            elif(key=='Speed'):
                self.speed=value
            elif(key=='STR'):
                self.strength=int(value)
            elif(key=='DEX'):
                self.dexterity=int(value)
            elif(key=='CON'):
                self.constitution=int(value)
            elif(key=='INT'):
                self.intelligence=int(value)
            elif(key=='WIS'):
                self.wisdom=int(value)
            elif(key=='CHA'):
                self.charisma=int(value)
            elif(key=='Skills'):
                self.skills=value
            elif(key=='Senses'):
                self.senses=value
            elif(key=='Languages'):
                self.languages=value
            elif(key=='Challenge'):
                vals = value.split('(')
                self.challenge=vals[0]
                self.experiencePoints=vals[1].replace(')','')
            elif(key=='Traits'):
                self.traits=value
            elif(key=='Actions'):
                self.strAction=value
                self.actions=self.generateActions(value)
            elif(key=='Legendary Actions'):
                self.strLegendaryActions=value
                self.legendaryActions=self.generateActions(value)

    #handles creating actions for the monster class. 
    #takes in the string representation of actions and returns an array of actionss
    def generateActions(self, stract):
        acts=[]
        for a in stract.split("</p>"):
            a=a+"</p>"
            act = action(a)
            if(act.name!="" and act.body!=""):
                acts.append(action(a))
        return acts

    ##Calculates the strength modifie
    def calcStrMod(self):
        return math.trunc((self.strength-10)/2)
    #calculates the dex modifier
    def calcDexMod(self):
        return math.trunc((self.dexterity-10)/2)
    #calculates the con modifier
    def calcConMod(self):
        return math.trunc((self.constitution-10)/2)
    #calculates the wis modifier
    def calcWisMod(self):
        return math.trunc((self.wisdom-10)/2)
    #calculates the int modifier
    def calcIntMod(self):
        return math.trunc((self.intelligence-10)/2)
    #calculates the cha modifier
    def calcChaMod(self):
        return math.trunc((self.charisma-10)/2)

    def __str__(self):
        return f"{self.name} {self.meta} {self.ac} {self.hp} {self.speed} {self.strength} {self.dexterity} {self.constitution} {self.intelligence} {self.wisdom} {self.charisma} {self.savingThrows} {self.skills} {self.damageImmunities} {self.senses} {self.challenge} {self.traits} {self.action} {self.legendaryActions} {self.img}"

    