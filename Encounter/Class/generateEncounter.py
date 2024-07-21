from .Encounter import Encounter
from .party import Party
import random
'''
import functools

from flask import (
    Blueprint, render_template #, flash, g, redirect, request, session, url_for
)
#from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('encounter', __name__, url_prefix='/encounter')
'''
class generateEncounter:
    monsters=[]
    enviornment=[]
    challengeRating=-1
    alignment=["unaligned","lawful good","neutral good","chaotic good","lawful neutral","neutral","chaotic neutral","lawful evil","neutral evil","chaotic evil"]
    sizeRange=['Tiny','Small','Medium','Large','Huge','Gargantuan']
    challengeRatingRange=[.125,.25,.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    chosenAlignment=[]
    chosenSize=[]
    chosenChallenge=[]
    filteredMonsters=[]
    party=Party
    encounters=[]
    
    #@bp.route('/encounter', methods=('GET', 'POST'))
    #def encounter():
    #    return render_template('encounter.html')

    def __init__(self, monsters):
        self.monsters=monsters
        self.filteredMonsters=monsters
        self.chosenSize=[]
        self.challengeRating=-1
        self.chosenAlignment=[]
        self.party=Party(0,0)
        self.enviornment=[]
        self.encounters=[]
        self.chosenChallenge=[]
        self.encounterCapacity=5

    #reset the filteredMonsters list to original monsters, and set all filters to default. 
    def resetFilters(self):
        self.filteredMonsters=self.monsters
        self.chosenAlignment=[]
        self.chosenSize=[]
        self.challengeRating=-1
        self.encounterCapacity=5

    def runFilter(self):
        mons=self.monsters
        #filter for challengeRating
        if self.chosenChallenge:
            aMons=[]
            for c in self.chosenChallenge:
                #print("chosen challenge:",c)
                for m in mons:
                    #print("checking these:",c,m.challenge)
                    if(float(c)==float(m.challenge)):
                        #print('appened mon in runfilter:',m.name,m.challenge)
                        aMons.append(m)
            #print('amons len',len(aMons))
            mons=aMons
        #filter for alignment
        if self.chosenAlignment:
            aMons=[]
            for a in self.chosenAlignment:
                for m in mons: 
                    if(self.normalizeString(m.alignment) == self.normalizeString(a)):
                        aMons.append(m)
            mons=aMons
        #filter for size
        if self.chosenSize:
            aMons=[]
            for s in self.chosenSize:
                #print("appended new size:", s)
                for m in mons:
                    if(self.normalizeString(s)==self.normalizeString(m.size)):
                        aMons.append(m)
            mons=aMons

        calcCap=self.party.calculateCapacity()
        print("calc cap:",calcCap)
        if calcCap!=0:
            aMons=[]
            for m in mons:
                if calcCap+2 >= float(m.challenge):
                    print("filtered monster from party", m.name, m.challenge)
                    aMons.append(m)
            
            mons=aMons
        #set the filtered Monsters to the temp array. 
        #print('Frm runFILTER: length of filteredMons,',len(self.filteredMonsters),'len of mons,',len(mons), 'len of monsters:',len(self.monsters))
        self.filteredMonsters=mons
        return mons

    #filter for the challengeRating, returns a list of creatures challenged at or below the cr rating.
    def setChallengeRating(self, cr):
        self.challengeRating=cr
        #print("watcha",cr)
        if float(cr) in self.challengeRatingRange:
            #print("what",cr)
            self.chosenChallenge.append(cr)
            return self.runFilter()#run filter and return result
        return []

    def setParty(self,party):
        self.party=party

    #filter for an indivdual alignment. 
    #if alignent is within the alignment list then run filter. else return an empty array
    def setAlignment(self,align):
        if align in self.alignment:
            self.chosenAlignment.append(align)
            return self.runFilter() #run filter and return result
        return []

    #set the size of the filtered out encounters
    def setSize(self,sz):
        if sz in self.sizeRange:
            self.chosenSize.append(sz)
            return self.runFilter()
        return []

    #removes a specified alignment filter
    def removeAlignmentFilter(self,filter):
        #remove alignment filter
        if filter in self.chosenAlignment:
            self.chosenAlignment.remove(filter)
            return self.runFilter()
        return self.filteredMonsters
    
    #removes a specified size filter
    def removeSizeFilter(self,filter):
        if filter in self.chosenSize:
            self.chosenSize.remove(filter)
            return self.runFilter()
        return self.filteredMonsters

    #normalizes string to help with formatting    
    def normalizeString(self,norm):
        return norm.replace(' ','').upper()

    def setEncounterCapacity(self, pts):
        self.encounterCapacity=pts
        return self.runFilter()

    #returns number of encounters based on filters and party
    def recommendEncounters(self,num):
        monslist=[]
        #encounterCapacity=5
        oldCR=self.challengeRating
        #print('filtered mons len',len(self.filteredMonsters))
        if self.party.calculateCapacity() != 0:
            #self.encounterCapacity=self.party.calculateCapacity()
            #print('encounterCapacity: ',encounterCapacity)
            monslist=self.setEncounterCapacity(self.party.calculateCapacity())
        enclist=[]
        #print('filtered mons len',len(self.filteredMonsters), 'mons list len:', len(monslist))

        for i in range(num):
            enc = Encounter([])
            while True and self.filteredMonsters:
                #monslist.append(self.randomMonster(self.filteredMonsters))
                #I want to add in a random number generator that will occasionally stop the program...
                enc.monsters.append(self.randomMonster(self.filteredMonsters))
                #print('encounter', i, enc)
                if enc.calculateMonsterChallenge()>=self.encounterCapacity-1:
                    enclist.append(enc)
                    break
            #grab a random monster from monster list, if it meets the challenge rating then return it, else pull another monster. 
            #asdf 
        #the exp function is x/2+50
        if self.challengeRating!=oldCR: self.setChallengeRating(oldCR)
        return enclist

    #this will create a random encounter with the provided inputs... 
    def randomMonster(self, mons):
        #i=int(random.random() * len(mons))
        #print('random int: ', i, 'returns: ', mons[i].name)
        #i = rand.randint(0,len(mons)-1)
        if mons:
            m=random.choice(mons)
            return m
    
        #print('random monster:', m.name)
        return [] #random.choice(mons) # mons[i]
        #loop through the monsters
      