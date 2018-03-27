import unittest
import main

class TestMain(unittest.TestCase):

    def test_get_boston_weather(self):
        result = main.get_boston_weather('42.3601', '-71.0589')
        self.assertIsNotNone(result)
