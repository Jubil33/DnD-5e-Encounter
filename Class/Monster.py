#Monster class:
# this class is defined as a monster it will include a couple of fields such as stat and monster
#Fields: Name, meta, AC, HP Speed, STR
#
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
    action=""
    legendaryActions=""
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
                self.action=value
            elif(key=='Legendary Actions'):
                self.legendaryActions=value

    #get name of monster
    def getName(self):
        return self.name

    def get_ac(self):
        return self.ac

    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_strength(self):
        return self.strength

    def get_dexterity(self):
        return self.dexterity

    def get_constitution(self):
        return self.constitution

    def get_intelligence(self):
        return self.intelligence

    def get_wisdom(self):
        return self.wisdom

    def get_charisma(self):
        return self.charisma

    def get_savingThrows(self):
        return self.savingThrows

    def get_damageImmunities(self):
        return self.damageImmunities

    def get_skills(self):
        return self.skills

    def get_senses(self):
        return self.senses

    def get_languages(self):
        return self.languages

    def get_traits(self):
        return self.traits

    def get_action(self):
        return self.action

    def get_legendaryActions(self):
        return self.legendaryActions

    def get_img(self):
        return self.img

    def get_challenge(self):
        return self.challenge
    
    def __str__(self):
        return f"{self.name} {self.meta} {self.ac} {self.hp} {self.speed} {self.strength} {self.dexterity} {self.constitution} {self.intelligence} {self.wisdom} {self.charisma} {self.savingThrows} {self.skills} {self.damageImmunities} {self.senses} {self.challenge} {self.traits} {self.action} {self.legendaryActions} {self.img}"

    