from Class.action import action

# Monster class:
# this class is defined as a monster it will include a couple of fields such as stat and monster
#Fields: Name, meta, AC, HP Speed, STR
 
class Monster:
    name=""
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

    def __init__(self,monsterDict):#, name, meta, AC, HP, Speed, STR, DEX, CON, INT, WIS, CHA, SThrows, Skills, DmgImmunities,Senses, Lang, Challenge, Traits, Actions, LegActions): #,img_URl):
        for key,value in monsterDict.items():
            #print(items)
            if(key=='name'):
                self.name=value
            elif(key=='meta'):
                self.meta=value
            elif(key=='Armor Class'):
                self.ac=value
            elif(key=='Hit Points'):
                self.hp=value
            elif(key=='Speed'):
                self.speed=value
            elif(key=='STR'):
                self.strength=value
            elif(key=='DEX'):
                self.dexterity=value
            elif(key=='CON'):
                self.constitution=value
            elif(key=='INT'):
                self.intelligence=value
            elif(key=='WIS'):
                self.wisdom=value
            elif(key=='CHA'):
                self.charisma=value
            elif(key=='Skills'):
                self.skills=value
            elif(key=='Senses'):
                self.senses=value
            elif(key=='Languages'):
                self.languages=value
            elif(key=='Challenge'):
                self.challenge=value
            elif(key=='Traits'):
                self.traits=value
            elif(key=='Actions'):
                self.strAction=value
                self.actions=self.generateActions(value)
            elif(key=='Legendary Actions'):
                self.strLegendaryActions=value

    def generateActions(self, stract):
        acts=[]
        for a in stract.split("</p>"):
            a=a+"</p>"
            act = action(a)
            if(act.name!="" and act.body!=""):
                acts.append(action(a))
                print(self.name, ': ' ,act.name, ': ', act.body)
        return acts

    def __str__(self):
        return f"{self.name} {self.meta} {self.ac} {self.hp} {self.speed} {self.strength} {self.dexterity} {self.constitution} {self.intelligence} {self.wisdom} {self.charisma} {self.savingThrows} {self.skills} {self.damageImmunities} {self.senses} {self.challenge} {self.traits} {self.action} {self.legendaryActions} {self.img}"

    