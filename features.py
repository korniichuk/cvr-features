# -*- coding: utf-8 -*-
# Name: features
# Version: 0.1a2
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal

from promovolt.readability import sentence_counter, word_counter


def rkmb(text, language='en'):
    """RKMB."""
    # Split text to sentences
    _, sentences_as_text = sentence_counter(text, language)

    # Split sentences to words
    sentences_as_words = []
    for sentence in sentences_as_text:
        _, words = word_counter(sentence, language)
        # Filter empty sentences
        if words:
            sentences_as_words.extend(words)

    num = 0
    flag = False
    for i in range(len(sentences_as_words)-1):
        if sentences_as_words[i][0] == sentences_as_words[i+1][0]:
            num += 1
            flag = True
            if i == len(sentences_as_words)-2:
                num += 1
        else:
            if flag:
                num += 1
            flag = False
    rkmb = 1 - (Decimal(num) / Decimal(len(sentences_as_words)))
    rkmb = float(rkmb)
    return rkmb
