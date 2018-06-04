# -*- coding: utf-8 -*-
"""
@author: SBOHORA
"""

def count_substring(string, sub_string):
    """
    Print the number of times that the substring occurs in the given string
    :param string: string is an input string
    :param sub_string: sub_string is a part of input string to be counted for its occurrence
    :return: returns swapped case
    Usage:
        s = 'GNCHCDCDC'
        count_substring(s, 'CDC')
    """
    sum_count = 0
    for i in range(len(string)):
        if string.startswith(sub_string, i):
            add = 1
            sum_count += add
    return sum_count  
