# -*- coding: utf-8 -*-
"""
@author: SBOHORA
"""
import re

def to_any_case(x, case = ['screaming_snake_case','all_caps','swap_case','flip_case','snake_case',
                           'lower_camel_case','upper_camel_case','upper_lower','parsed_case',
                           'small_camel','big_camel','lower_camel','upper_camel', 'none']):
    """
    Convert variable names to any case. for example, snake_Case is a variable naming style separatd by '_'
    :param x: x is an input string (seprated by multiple spaces, underscores or capitalization)
    :param case: case is to specify the output case type 
    :return: returns snake_case
    Usage:
        x = "this Is a Strange_string 2"
        to_any_case(x, case = 'screaming_snake_case')
        to_any_case(x, case = 'snake_case')
        to_any_case(x, case = 'lower_camel_case')
        to_any_case(x, case = 'upper_camel_case')
        to_any_case(x, case = 'upper_lower')
        to_any_case(x, case = 'lower_upper')
        to_any_case(x, case = "parsed_case")
        to_any_case(x, case = "swap_case")
        to_any_case(x, case = "all_caps")
        to_any_case(x, case = "proper_snake_case")
        to_any_case(x, case = "none")
        to_any_case(x)
    """
    
    if case == 'snake_case':
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
            
    elif case == 'lower_camel_case' or case =='small_camel' or case == 'lower_camel':
        s = ''.join([char if char.isalpha() or char.isdigit() else " " for char in x]).split()
        x = [x.title() for x in s]
        x = [x[0].lower()] + x[1:]
        x = ''.join(x)
            
    elif case == 'screaming_snake_case' or case == 'all_caps':
        string = re.findall('_', x)
        if len(string) > 1:
            x = re.sub('_+','',x)
        else:
            x = x
        if any(x.lower()):
            x = '_'.join(x.split()).upper()
        else:
            x = ' '.join(x.split())
            x = '_'.join(x.split()).upper()
            
    elif case == 'upper_camel_case' or case == 'big_camel' or case == 'upper_camel':
        s = ''.join([char if char.isalpha() or char.isdigit() else " " for char in x]).split()
        x = [x.title() for x in s]
        x = ''.join(x)
                    
    elif case == 'upper_lower':
        x = ''.join([char if char.isalpha() or char.isdigit() else " " for char in x]).lower().split()
        x[::2] = [i.upper() for i in x[::2]]
        x = ''.join(x)
        
    elif case == 'lower_upper':
        x = ''.join([char if char.isalpha() or char.isdigit() else " " for char in x]).upper().split()
        x[::2] = [i.lower() for i in x[::2]]
        x = ''.join(x)
        
    elif case =='parsed_case':
        string = re.findall('_', x)
        if len(string) > 1:
            x = re.sub('_+','',x)
        else:
            x = x
        x = '_'.join(x.split())
        
    elif case == 'swap_case' or case == 'flip_case':
        lst = []
        for i in x:
            if i.islower():
                lst.append(i.upper())
                x = ''.join(lst)
            else:
                lst.append(i.lower())
                x = ''.join(lst)
                
    elif case == 'proper_snake_case':
        s = ''.join([char if char.isalpha() or char.isdigit() else " " for char in x]).split()
        x = [x.title() for x in s]
        x = '_'.join(x)
    else:
        print('WARNING: You did not specify the case. Therefore, original string is returned.')
        x
    return(x)
