# -*- coding: utf-8 -*-
# Name: languagetool
# Version: 0.3a1
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal
import time

from nltk import tokenize
import requests

from promovolt.readability import word_counter

# $ python3 -m nltk.downloader punkt


def grammar_mistakes(
        text, limit_bytes=5120, language='en-US', language_code='en'):
    """Grammar mistakes.

    Returns:
        Number of grammar mistakes.
        Average number of Grammar Mistakes per Sentence.
        Number of Grammar Mistakes per total number of Words in text.

    Docs: https://languagetool.org/http-api/
    """

    def prepare_text(text):
        while len(bytes(text, 'utf-8')) > limit_bytes:
            sentences = tokenize.sent_tokenize(text)
            sentences = sentences[:-1]
            text = ' '.join(sentences)
        return text

    agms = None
    gmw = None

    text = prepare_text(text)

    sentences_num = len(tokenize.sent_tokenize(text))
    words_num, _ = word_counter(text, language_code)

    data = {'text': text, 'language': language}
    r = requests.post('https://api.languagetool.org/v2/check', data=data)
    gm_num = len(r.json()['matches'])

    if sentences_num != 0:
        agms = Decimal(gm_num) / Decimal(sentences_num)
        agms = float(agms)

    if words_num != 0:
        gmw = Decimal(gm_num) / Decimal(words_num)
        gmw = float(gmw)

    time.sleep(4)

    return gm_num, agms, gmw
