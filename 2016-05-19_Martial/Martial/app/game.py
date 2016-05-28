from app.screen import Screen
from app.deck import Deck
from app.hand import Hand
from app.zone import Zone

class Game(object):

    def __init__(self):
        self.scr = Screen()
        self.shared_deck = Deck("data/shared_deck")
        self.player_hand = Hand("data/starting_options")
        self.player_deck = Deck()
        self.player_discarded_cards = Zone()

    def drawPlayerHand(self):
        self.player_deck

    def turn(self):
        pass

    def paint(self):
        pass
    
    def end(self):
        self.scr.end()
