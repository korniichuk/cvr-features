# -*- coding: utf-8 -*-
# Name: features
# Version: 0.1a3
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal

from promovolt.readability import sentence_counter, word_counter


def pus(text, language_code='en'):
    """PUS -- Percentage of Unique Sentences."""
    pus = None

    # Filter empty sentences
    _, sentences = sentence_counter(text, language_code)
    sentences = list(filter(None, sentences))

    sentences_num = len(sentences)
    unique_sentences_num = len(set(sentences))

    if sentences_num != 0:
        pus = unique_sentences_num / sentences_num
    return pus


def rkmb(text, language_code='en'):
    """RKMB."""
    # Split text to sentences
    _, sentences_as_text = sentence_counter(text, language_code)

    # Split sentences to words
    sentences_as_words = []
    for sentence in sentences_as_text:
        _, words = word_counter(sentence, language_code)
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
