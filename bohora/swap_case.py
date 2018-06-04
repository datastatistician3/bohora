# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:58:22 2018

@author: SBOHORA
"""

def swap_case(x):
    """
    You are given a string and your task is to swap cases. In other words, convert all lowercase letters 
    to uppercase letters and vice versa.
    :param x: x is an input string
    :return: returns swapped case
    Usage:
        swap_case('HackerRank.com presents "Pythonist 2".')
    """
    lst = []
    for i in x:
        if i.islower():
            lst.append(i.upper())
            swapped = ''.join(lst)
        else:
            lst.append(i.lower())
            swapped = ''.join(lst)
    return swapped