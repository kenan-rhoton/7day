import unittest
from app.game import Game
from app.deck import Deck
from app.hand import Hand

class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        self.game.end()


    def test_game_launches_and_shows_message(self):
        self.assertIsInstance(self.game.getSharedDeck(),Deck)
        self.assertIn("Pick your starting card groups",self.game.screenDump())

    def test_game_offers_you_a_starting_hand(self):
        self.game.pickRandomStart()
        self.assertIsInstance(self.game.getPlayerHand(),Hand)
        self.assertIsInstance(self.game.getPlayerDeck(),Deck)
        self.assertIn("Your hand",self.game.screenDump())



if __name__ == '__main__':
    unittest.main()
