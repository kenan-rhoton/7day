from app.screen import Screen
from app.deck import Deck
from app.hand import Hand

class Game(object):

    def __init__(self):
        self.scr = Screen()
        self.shared_deck = Deck("data/shared_deck")
        self.player_hand = Hand()
        self.player_deck = Deck()
        self.scr.put("Pick your starting card groups")

    #Test helpers

    def pickRandomStart(self):
        self.scr.put("Your hand")
        pass

    def screenDump(self):
        return self.scr.dump()

    #Getters

    def getSharedDeck(self):
        return self.shared_deck

    def getPlayerHand(self):
        return self.player_hand

    def getPlayerDeck(self):
        return self.player_deck

    def end(self):
        self.scr.end()
