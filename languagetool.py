# -*- coding: utf-8 -*-
# Name: languagetool
# Version: 0.1a1
# Owner: Ruslan Korniichuk
# Maintainer(s):

import time

import requests


def count_grammar_mistakes(text, limit=5120, language_code='en-US'):
    """Get number of grammar mistakes.

    Docs: https://languagetool.org/http-api/
    """

    def prepare_text(text):

        while len(bytes(text, 'utf-8')) > limit:
            text = text[:-1]
        return text

    text = prepare_text(text)

    data = {'text': text, 'language': language_code}
    r = requests.post('https://api.languagetool.org/v2/check', data=data)
    time.sleep(4)
    return len(r.json()['matches'])
