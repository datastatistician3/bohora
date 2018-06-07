# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:33:10 2018

@author: SBOHORA
"""

def kmers_of(x, k, remove_space = False):
    """
    Return the k-mers (substrings of size k) of the string x, or
    return the string x itself if it is shorter than k.
    :param k: the size of the substrings, an integer
    :param x: a character string
    :param remove_space_space: Argument whether to remove space or not
    :return kmers_of: a character vector of the k-mers of x
    Usage:
        x = 'Find three kmers'
        kmers_of(x,3, remove_space=True)
    """
    if remove_space:
        x = x.strip().replace(" ", "")
    else:
        x = x
    if len(x) < k:
        x
    else:
        x = [x[i:i+k:1] for i in range(len(x))]
        x = [i for i in x if len(i) == k]
    return x






