from Class.Encounter import Encounter

class generateEncounter:
    monsters=[]
    enviornment=''
    challengeRating=-1
    alignment=["unaligned","lawful good","neutral good","chaotic good","lawful neutral","neutral","chaotic neutral","lawful evil","neutral evil","chaotic evil"]
    sizeRange=['Tiny','Small','Medium','Large','Huge','Gargantuan']
    chosenAlignment=[]
    chosenSizeRange=[]
    filteredMonsters=[]

    def __init__(self, monsters):
        self.monsters=monsters
        self.filteredMonsters=monsters

    #this will reset the filteredMonsters list to include the parameters for filtering. 
    def resetFilters(self):
        self.filterMonsters=self.monsters

    def runFilter(self):
        mons=self.monsters
        
        #check for challengeRating
        if self.challengeRating != -1:
            aMons=[]
            for m in mons:
                if(self.challengeRating>=m.challenge):
                    aMons.append(m)
            mons=aMons
        
        #check for alignment this currently only works for alignment.
        if self.chosenAlignment:
            aMons=[]
            for a in self.chosenAlignment:
                #print('asdfasdf - filtering for:',a,'alignment')
                for m in mons: #filter out monsters that don't fit with the alignment
                    #print('comparing', m.name, self.normalizeString(m.alignment), 'with',self.normalizeString(a))

                    if(self.normalizeString(m.alignment) == self.normalizeString(a)):
                        #print()
                        aMons.append(m)
                #print('exited from alignment')
            mons=aMons

        #check for size. It will look  similar to the alignment

        #set the filtered Monsters to the temp array. 
        self.filteredMonsters=mons
        return mons

    #filter for the challengeRating, returns a list of creatures challenged at or below the cr rating.
    def setChallengeRating(self, cr):
        self.challengeRating=cr
        #run filter and return result
        return self.runFilter()
    
    #filter for an indivdual alignment. 
    #if alignent is within the alignment list then run filter. else return an empty array
    def setAlignment(self,align):
        if align in self.alignment:
            self.chosenAlignment.append(align)
            print('alignments chosen: ', self.chosenAlignment)
            #run filter and return result
            return self.runFilter()
        return []

    #set the size of the filtered out encounters
    def setSize(self,sz):
        asdf=0

    #removes a specified filter. 
    def removeFilter(self,filterType,filter):
        asdf=0

    #normalizes string to help with formatting    
    def normalizeString(self,norm):
        return norm.replace(' ','').upper()

    #a function to return the filters on within the string

    def randomEncounter():
        asdf=0 
        #loop through the monsters

    