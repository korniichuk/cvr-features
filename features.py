# -*- coding: utf-8 -*-
# Name: features
# Version: 0.1a18
# Owner: Ruslan Korniichuk
# Maintainer(s):

from decimal import Decimal
from fractions import Fraction
import re

from gensim.parsing.preprocessing import STOPWORDS
from nltk.corpus import stopwords
import spacy

from promovolt.readability import sentence_counter, word_counter

# $ python3 -m spacy download en_core_web_lg


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


def acds(text, transition_words, language_code='en'):
    """Average number of Cohesive Devices (transition words and phrases)
       per Sentence.
    """

    acds = None
    transition_words_num = 0

    sentences_num, _ = sentence_counter(text, language_code)

    tmp = text
    for word in transition_words:
        pattern = r'\b(%s)\b' % word
        r = re.split(pattern, tmp.lower(), maxsplit=1)
        while len(r) != 1:
            transition_words_num += 1
            tmp = r[0] + r[2]
            r = re.split(pattern, tmp.lower(), maxsplit=1)

    if sentences_num != 0:
        acds = Decimal(transition_words_num) / Decimal(sentences_num)
        acds = float(acds)
    return acds


def apvs(text, nlp, language_code='en'):
    """Average number of Passive Voice constructions per Sentence."""

    apvs = None

    matcher = spacy.matcher.Matcher(nlp.vocab)
    pattern = [{'DEP': 'nsubjpass'},
               {'DEP': 'aux', 'OP': '*'},
               {'DEP': 'auxpass'},
               {'TAG': 'VBN'}]
    matcher.add('Passive', [pattern])

    doc = nlp(text)
    ppv_num = len(matcher(doc))

    sentences_num = len(list(doc.sents))

    if sentences_num != 0:
        apvs = Decimal(ppv_num) / Decimal(sentences_num)
        apvs = float(apvs)
    return apvs


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


def get_stop_words():
    """Get stop words."""

    nltk_stopwords = stopwords.words('english')  # 179
    gensim_stopwords = list(STOPWORDS)  # 337

    stop_words = nltk_stopwords + gensim_stopwords
    stop_words = set(stop_words)  # 390
    return stop_words


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


def psw2(text, stop_words, language_code='en'):
    """PSW2 -- Percentage of Stop Words."""

    psw2 = None
    stop_words_num = 0

    words_num, words = word_counter(text, language_code)
    for word in words:
        word_lower = word.lower().strip()
        if word_lower in stop_words:
            stop_words_num += 1

    if words_num != 0:
        psw2 = Decimal(stop_words_num) / Decimal(words_num)
        psw2 = float(psw2)
    return psw2


def ptww(text, transition_words, language_code='en'):
    """PTW -- Percentage of Transition Words per Word."""
    # TODO

    ptw = None
    transition_words_num = 0

    words_num, _ = word_counter(text, language_code)

    tmp = text
    for word in transition_words:
        pattern = r'\b(%s)\b' % word
        r = re.split(pattern, tmp.lower(), maxsplit=1)
        while len(r) != 1:
            transition_words_num += 1
            tmp = r[0] + r[2]
            r = re.split(pattern, tmp.lower(), maxsplit=1)

    if words_num != 0:
        ptw = Decimal(transition_words_num) / Decimal(words_num)
        ptw = float(ptw)
    return ptw


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


def pvw(text, nlp, language_code='en'):
    """Number of Passive Voice constructions per total number of Words
       in text.
    """

    pvw = None

    matcher = spacy.matcher.Matcher(nlp.vocab)
    pattern = [{'DEP': 'nsubjpass'},
               {'DEP': 'aux', 'OP': '*'},
               {'DEP': 'auxpass'},
               {'TAG': 'VBN'}]
    matcher.add('Passive', [pattern])

    doc = nlp(text)
    ppv_num = len(matcher(doc))

    words_num, _ = word_counter(text, language_code)

    if words_num != 0:
        pvw = Decimal(ppv_num) / Decimal(words_num)
        pvw = float(pvw)
    return pvw


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
        rkmb = Fraction(1, 1) - (sum(tmp) / Fraction(len(tmp), 1))
        rkmb = float(rkmb)
    else:
        rkmb = 1.0
    return rkmb
