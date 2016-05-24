from app.card import Card

class Zone(object):

    def __init__(self, source = ""):

        self.cardlist = []
        self.discard = []

        if source != "":
            self.load(source)

    def size(self):
        return self.cardlist.__len__()

    def load(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                data = line.split(";",1)
                if data.__len__() < 2:
                    return
                self.cardlist.append(Card(data[0],data[1]))

    def containsCardNames(self, names):
        for name in names:
            found = False
            for card in self.cardlist:
                if name == card.getName():
                    found = True
                    break
            if found == False:
                return False
        return True
