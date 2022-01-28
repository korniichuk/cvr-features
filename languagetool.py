# -*- coding: utf-8 -*-
# Name: languagetool
# Version: 0.2a1
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal
import time

from nltk import tokenize
import requests

# $ python3 -m nltk.downloader punkt


def agms(text, limit_bytes=5120, language_code='en-US'):
    """Average number of Grammar Mistakes per Sentence.

    Docs: https://languagetool.org/http-api/
    """

    def prepare_text(text):
        while len(bytes(text, 'utf-8')) > limit_bytes:
            sentences = tokenize.sent_tokenize(text)
            sentences = sentences[:-1]
            text = ' '.join(sentences)
        return text

    agms = None

    text = prepare_text(text)

    sentences_num = len(tokenize.sent_tokenize(text))

    data = {'text': text, 'language': language_code}
    r = requests.post('https://api.languagetool.org/v2/check', data=data)
    gm_num = len(r.json()['matches'])

    if sentences_num != 0:
        agms = Decimal(gm_num) / Decimal(sentences_num)
        agms = float(agms)

    time.sleep(4)

    return agms
