import unittest
from app.card import Card
from app.screen import Screen

class TestCard(unittest.TestCase):

    def test_card_name_assigned_correctly(self):
        card = Card("Potato","Used to make pie")
        self.assertEqual(card.name, "Potato")

    def test_card_description_assigned_correctly(self):
        card = Card("Potato","Used to make pie")
        self.assertEqual(card.description, "Used to make pie")



if __name__ == '__main__':
    unittest.main()
