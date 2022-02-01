# -*- coding: utf-8 -*-
# Name: writer_invariant
# Version: 0.1a2
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal

from promovolt.readability import sentence_counter, word_counter


def aas(text, nlp, language_code='en'):
    """Average number of Adjectives per Sentence."""

    aas = None

    doc = nlp(text)

    sentences_num, _ = sentence_counter(text, language_code)

    adjectives = [token.lemma_ for token in doc if token.pos_ == 'ADJ']
    adjectives_num = len(adjectives)

    if sentences_num != 0:
        aas = Decimal(adjectives_num) / Decimal(sentences_num)
        aas = float(aas)
    return aas


def ans(text, nlp, language_code='en'):
    """Average number of Nouns per Sentence."""

    ans = None

    doc = nlp(text)

    sentences_num, _ = sentence_counter(text, language_code)

    nouns = [token.lemma_ for token in doc if token.pos_ == 'NOUN']
    nouns_num = len(nouns)

    if sentences_num != 0:
        ans = Decimal(nouns_num) / Decimal(sentences_num)
        ans = float(ans)
    return ans


def avs(text, nlp, language_code='en'):
    """Average number of Verbs per Sentence."""

    avs = None

    doc = nlp(text)

    sentences_num, _ = sentence_counter(text, language_code)

    verbs = [token.lemma_ for token in doc if token.pos_ == 'VERB']
    verbs_num = len(verbs)

    if sentences_num != 0:
        avs = Decimal(verbs_num) / Decimal(sentences_num)
        avs = float(avs)
    return avs


def pa(text, nlp, language_code='en'):
    """Percentage of Adjectives in text."""

    pa = None

    doc = nlp(text)

    words_num, _ = word_counter(text, language_code)

    adjectives = [token.lemma_ for token in doc if token.pos_ == 'ADJ']
    adjectives_num = len(adjectives)

    if words_num != 0:
        pa = Decimal(adjectives_num) / Decimal(words_num)
        pa = float(pa)
    return pa


def pn(text, nlp, language_code='en'):
    """Percentage of Nouns in text."""

    pn = None

    doc = nlp(text)

    words_num, _ = word_counter(text, language_code)

    nouns = [token.lemma_ for token in doc if token.pos_ == 'NOUN']
    nouns_num = len(nouns)

    if words_num != 0:
        pn = Decimal(nouns_num) / Decimal(words_num)
        pn = float(pn)
    return pn


def pv(text, nlp, language_code='en'):
    """Percentage of Verbs in text."""

    pv = None

    doc = nlp(text)

    words_num, _ = word_counter(text, language_code)

    verbs = [token.lemma_ for token in doc if token.pos_ == 'VERB']
    verbs_num = len(verbs)

    if words_num != 0:
        pv = Decimal(verbs_num) / Decimal(words_num)
        pv = float(pv)
    return pv
