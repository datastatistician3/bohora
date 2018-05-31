# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:23:08 2018

@author: SBOHORA
"""
import string

def count_words_in_string(x, remove_punctuation = False):
    """
    Count the number of words in a given string
    :param x: x is an input string (seprated by multiple spaces)
    :param remove_punctuation: remove_punctuation is a boolean variable whether to remove punctuation or not
    :return: returns each unique word and its occurrences
    Usage:
        x = "This is a string. This is a a word. hora?"
        count_words_in_string(x)
        count_words_in_string(x, remove_punctuation=True)
    """
    counts = dict()    
    if remove_punctuation:
        s = ''.join(i for i in x if i not in string.punctuation)
#        z=''
#        for i in x:
#            if i not in string.punctuation:
#                z += i
#            z
    else:
        s = x
        
    result = s.split(' ')
    for word in result:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1 
    return(counts)
