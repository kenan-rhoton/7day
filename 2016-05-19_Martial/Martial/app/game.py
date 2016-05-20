from app.screen import Screen
from app.deck import Deck

class Game(object):

    def __init__(self):
        self.scr = Screen()
        self.shared_deck = Deck()
    
    def pickRandomStart(self):
        pass

    def getSharedDeck(self):
        return self.shared_deck

    def getPlayerHand(self):
        pass

    def end(self):
        self.scr.end()
