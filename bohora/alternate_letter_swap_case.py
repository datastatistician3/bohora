# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:51:28 2018

@author: sbohora
"""

def alternate_letter_swap_case(args):
    return(''.join([args[i].lower() if i % 2 == 0 else args[i].upper() for i in range(len(args))]))

args = "Anthropomorphism"
alternate_letter_swap_case(args)


lst = [2,3,4,3]
#subset
[x for x in lst if x % 2 == 0]
#recode
[x if x % 2 == 0 else 'fdf' for x in lst]
