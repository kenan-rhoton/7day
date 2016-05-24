import unittest
from app.screen import Screen

class TestScreen(unittest.TestCase):

    def setUp(self):
        self.screen = Screen()

    def tearDown(self):
        self.screen.end()

    def test_screen_printing_capabilities(self):
        self.screen.put("ASDFQWERTY")
        self.assertIn("ASDFQWERTY",self.screen.dump())


if __name__ == '__main__':
    unittest.main()
