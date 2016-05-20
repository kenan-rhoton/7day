from app.card import Card
from app.zone import Zone

class Deck(Zone):

    def __init__(self, source=""):

        Zone.__init__(self)

        if source != "":
            with open(source, 'r') as f:
                for line in f:
                    data = line.split(";",1)
                    self.cardlist.append(Card(data[0],data[1]))

    def addCardBlock(self, name):
        pass
