import unittest
from textblob import TextBlob
from src.utils import calculate_sentiment


class TestCalculateSentiment(unittest.TestCase):
    def test_calculate_sentiment(self):
        # Define a test case
        text = "This is a good day."

        # Calculate the sentiment score using the function
        sentiment_score = calculate_sentiment(text)

        # Calculate the expected sentiment score using TextBlob directly
        expected_score = TextBlob(text).sentiment.polarity

        # Assert that the two scores are the same
        self.assertEqual(sentiment_score, expected_score)


if __name__ == '__main__':
    unittest.main()
