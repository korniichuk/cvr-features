# -*- coding: utf-8 -*-
# Name: features
# Version: 0.1a4
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal
from fractions import Fraction

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


def rkmb1(text, language_code='en'):
    """RKMB ver. 1."""
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


def rkmb2(text, language_code='en'):
    """RKMB ver. 2."""
    if (not text) or (not isinstance(text, str)):
        return None

    # Split text to sentences
    _, sentences_as_text = sentence_counter(text, language_code)

    if not sentences_as_text:
        return None

    # Split sentences to words
    sentences_as_words = []
    for sentence in sentences_as_text:
        _, words = word_counter(sentence, language_code)
        # Filter empty sentences
        if words:
            sentences_as_words.extend(words)

    if not sentences_as_words:
        return None

    repetitions = []
    pos = 0
    neg = 0
    flag = False
    for i in range(len(sentences_as_words)-1):
        if sentences_as_words[i][0] == sentences_as_words[i+1][0]:
            pos += 1
            flag = True
            if i == len(sentences_as_words)-2:
                pos += 1
                repetitions.append(pos)
                pos = 0
        else:
            neg += 1
            if flag:
                pos += 1
                repetitions.append(pos)
                pos = 0
            flag = False

    if repetitions:
        tmp = []
        for repetition in repetitions:
            denumerator = (repetition + len(sentences_as_words) -
                           sum(repetitions))
            val = Fraction(repetition, denumerator)
            tmp.append(val)
        rkmb = 1 - float(sum(tmp) / len(tmp))
    else:
        rkmb = 1.0
    return rkmb
