import unittest
from app.deck import Deck

class TestDeck(unittest.TestCase):

    def test_deck_loads_cards_correctly(self):
        deck = Deck()
        deck.load('data/test_deck')
        self.assertTrue(deck.containsCardNames(["Asahura Niton", "Michelangelo Spazzi", "Noyomura Je"]))


