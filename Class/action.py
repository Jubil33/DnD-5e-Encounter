#action class: takes in a str for the action and sets the name and body to the corresponding fields
from html.parser import HTMLParser

class action:
    strAction=""
    aType=""
    name=""
    body=""
    
    # all attributes are contained within <p> tags
    # <strong> tag symbolizes the title for the action
    # then the information is between </em> and </p>

    def __init__(self, saction):
        self.strAction=saction
        #how to set the the name
        #how to set the body?

    #def generateAction(self):
    #    parsed = HTMLParser.feed(self.strAction)
        
    