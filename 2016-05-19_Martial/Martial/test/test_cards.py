import unittest
from app.card import Card
from app.screen import Screen

class TddInPythonExample(unittest.TestCase):

    def setUp(self):
        self.screen = Screen()

    def tearDown(self):
        self.screen.end()


    def test_card_object_is_created(self):
        card = Card("Potato","Used to make pie")
        self.assertEqual(card.name, "Potato")
        self.assertEqual(card.description, "Used to make pie")

    def test_card_object_is_printed(self):
        card = Card("Potato","Used to make pie")
        card.paint(self.screen)
        self.assertIn("Potato",self.screen.dump())



if __name__ == '__main__':
    unittest.main()
