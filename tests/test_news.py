import unittest

from client import News

class NewsTest(unittest.TestCase):
    def test_country_headlines(self):
        client = News()
        headlines = client.country_headlines("fr") # list[string]
        self.assertIsInstance(headlines, list)
        self.assertGreater(len(headlines), 0)
        self.assertIsInstance(headlines[0], str)

