# -*- coding: utf-8 -*-
"""
Created on Wed May 30 08:59:17 2018

@author: SBOHORA
"""
import re
def snake_case(x):
    """
    Convert variable names to snake_case. Snake_Case is a variable naming style separatd by '_'
    :param x: x is an input string (seprated by multiple spaces, underscores or capitalization)
    :return: returns snake_case
    Usage:
        x = "First           Variable"
        snake_case(x)
        y = "SecondVariable"
        snake_case(y)
        z = "Third______Variable"
        snake_case(z)
        b = ["First           Variable","HiHello"]
        [snake_case(x) for x in b]
    """
    string = re.findall('_', x)
    if len(string) > 1:
        x = re.sub('_+','',x)
    else:
        x = x
    if any(x.upper()):
        x = re.sub(r'([^A-Z])([A-Z])', r'\1 \2', x)
        x = '_'.join(x.split()).lower()
    else:
        x = ' '.join(x.split())
        x = '_'.join(x.split()).lower()
    return(x)
