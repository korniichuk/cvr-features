# -*- coding: utf-8 -*-
# Name: features
# Version: 0.1a1
# Owner: Ruslan Korniichuk
# Maintainer(s):

from promovolt.readability import word_counter


def mbrk(sentences, language='en'):
    """MBRK."""
    # Filter empty sentences
    sentences = list(filter(None, sentences))

    num = 0
    flag = False
    for i in range(len(sentences)-1):
        _, words_current = word_counter(sentences[i], language)
        _, words_next = word_counter(sentences[i+1], language)
        if words_current[0] == words_next[0]:
            num += 1
            flag = True
            if i == len(sentences)-2:
                num += 1
        else:
            if flag:
                num += 1
            flag = False
    mbrk = (num / len(sentences)) * 100
    return mbrk
