# -*- coding: utf-8 -*-
# Name: comprehend
# Version: 0.1a2
# Owner: Ruslan Korniichuk
# Maintainer(s):

import boto3


def get_sentiment(text, language_code='en'):
    """Get sentiment.

    Inspects text and returns an inference of the prevailing sentiment
    (positive, neutral, mixed, or negative).

    Args:
        text: UTF-8 text string. Each string must contain fewer that
              5,000 bytes of UTF-8 encoded characters (required | type: str).
        language_code: language of text (not required | type: str |
                       default: 'en').

    Returns:
        sentiment: sentiment: positive, neutral, mixed, or negative
                   (type: str).
    """

    def prepare_text(text):

        while len(bytes(text, 'utf-8')) > 4999:
            text = text[:-1]
        return text

    comprehend = boto3.client('comprehend')
    text = prepare_text(text)

    try:
        r = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    except Exception as e:
        raise e
    sentiment = r['Sentiment'].lower()
    return sentiment

# Example. Get sentiment of text below:
# "I ordered a small and expected it to fit just right but it was a little bit
# more like a medium-large. It was great quality. It's a lighter brown than
# pictured but fairly close. Would be ten times better if it was lined with
# cotton or wool on the inside."
# text = "I ordered a small and expected it to fit just right but it was a \
#         little bit more like a medium-large. It was great quality. It's a \
#         lighter brown than pictured but fairly close. Would be ten times \
#         better if it was lined with cotton or wool on the inside."
# get_sentiment(text)
