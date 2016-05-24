import unittest
from app.game import Game
from app.deck import Deck
from app.hand import Hand

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        self.game.end()

    def test_game_autogenerates_shared_deck(self):
        self.assertIsInstance(self.game.shared_deck,Deck)

    def test_game_autogenerates_starting_hand(self):
        self.assertIsInstance(self.game.player_hand,Hand)

    def test_game_loads_starting_hand_properly(self):
        phand = self.game.player_hand
        self.assertTrue(phand.containsCardNames(["Fuerte","Rápido","Técnico","Resistente"]))

if __name__ == '__main__':
    unittest.main()
