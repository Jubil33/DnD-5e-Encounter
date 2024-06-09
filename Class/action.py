#action class: takes in a str for the action and sets the name and body to the corresponding fields
import re

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
        self.generateAction()

    def generateAction(self):
        #parsed = HTMLParser.feed(self.strAction)
        #actionSplit = self.strAction.split('</p>')
        #delim='</p>'
        #for a in actionSplit:
            #a+delim
        title_pattern = re.compile(r'<strong>(.*?)</strong>', re.DOTALL)
        data_pattern = re.compile(r'</em>(.*?)</p>', re.DOTALL)

        # Extract title
        title_match = title_pattern.search(self.strAction)
        self.name = title_match.group(1).strip() if title_match else ""

        data_match = data_pattern.search(self.strAction)
        self.body = data_match.group(1).strip() if data_match else ""

        #clean up data
        if self.name!="":
            self.name = re.sub(r'<.*?>', '', self.name)
        if self.body!="":
            self.body = re.sub(r'<.*?>', '', self.body)
        
    def __str__(self) -> str:
        return f"{self.name} {self.body}"