from app.card import Card

class Deck(object):

    def __init__(self, source=""):

        self.cardlist = []
        self.discard = []
        
        if source != "":
            with open(source, 'r') as f:
                for line in f:
                    data = line.split(";",1)
                    self.cardlist.append(Card(data[0],data[1]))

    def addCardBlock(self, name):
        pass

    def addCard(self, name):
        pass
