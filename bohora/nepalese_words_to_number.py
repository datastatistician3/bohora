# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:23:55 2018

@author: sbohora
"""

import re

def nepalese_words_to_number(x):
    """
    This method allows you to translate to integer numerical words spelled in Nepali.
    Text must be previously cleaned & removed extraneous words or symbols.
    :param x: x is an input string
    :return: returns an integer value
    Usage:
        x = "ek karod paanch hajaar paanch saya paanch"  # 1505
        nepalese_words_to_number(x)
    """
    x = x.lower()
    x = re.sub("soonya",             "+0" , x)     
    x = re.sub("ek",                 "+1" , x)     
    x = re.sub("dui",                "+2" , x)     
    x = re.sub("tin",                "+3" , x)     
    x = re.sub("char",               "+4" , x)     
    x = re.sub("paanch",             "+5" , x)     
    x = re.sub("chha",               "+6" , x)     
    x = re.sub("sat",                "+7" , x)     
    x = re.sub("aath",               "+8" , x)     
    x = re.sub("nau",                "+9" , x)     
    x = re.sub("das",               "+10" , x)     
    x = re.sub("eghaara",           "+11" , x)     
    x = re.sub("barha",             "+12" , x)     
    x = re.sub("terha",             "+13" , x)     
    x = re.sub("chaudha",           "+14" , x)     
    x = re.sub("pandhra",           "+15" , x)     
    x = re.sub("sorha",             "+16" , x)     
    x = re.sub("satra",             "+17" , x)     
    x = re.sub("athara",            "+18" , x)     
    x = re.sub("unnais",            "+19" , x)     
    x = re.sub("bis",               "+20" , x)     
    x = re.sub("ekkais",            "+21" , x)     
    x = re.sub("baais",             "+22" , x)     
    x = re.sub("teis",              "+23" , x)     
    x = re.sub("chaubis",           "+24" , x)     
    x = re.sub("pachchis",          "+25" , x)     
    x = re.sub("chhabbis",          "+26" , x)     
    x = re.sub("sattais",           "+27" , x)     
    x = re.sub("aththais",          "+28" , x)     
    x = re.sub("unantis",           "+29" , x)     
    x = re.sub("tis",               "+30" , x)     
    x = re.sub("ekkattis",          "+31" , x)     
    x = re.sub("battis",            "+32" , x)     
    x = re.sub("tettis",            "+33" , x)     
    x = re.sub("chauntis",          "+34" , x)     
    x = re.sub("paintis",           "+35" , x)     
    x = re.sub("chhattis",          "+36" , x)     
    x = re.sub("saitis",            "+37" , x)     
    x = re.sub("athtis",            "+38" , x)     
    x = re.sub("unnanchaalis",      "+39" , x)     
    x = re.sub("chalees",           "+40" , x)     
    x = re.sub("ekchalees",         "+41" , x)     
    x = re.sub("bayalees",          "+42" , x)     
    x = re.sub("triyalees",         "+43" , x)     
    x = re.sub("chawaalees",        "+44" , x)     
    x = re.sub("paitaalees",        "+45" , x)     
    x = re.sub("chhayaalees",       "+46" , x)     
    x = re.sub("sacchaalees",       "+47" , x)     
    x = re.sub("athchaalees",       "+48" , x)     
    x = re.sub("unanchas",          "+49" , x)     
    x = re.sub("pachas",            "+50" , x)         
    x = re.sub("saya",              ")*(100)+(0", x)         
    x = re.sub("hajaar",            ")*(1000)+(0", x)         
    x = re.sub("lakh",              ")*(100000)+(0", x)
    x = re.sub("karod",             ")*(10000000)+(0", x)     
    x = re.sub("arba",              ")*(1000000000)+(0", x)
    x = re.sub("kharaba",           ")*(100000000000)+(0", x)    
    x = re.sub("nil",               ")*(10000000000000)+(0", x)
    x = re.sub("padhna",            ")*(1000000000000000)+(0", x)
    x = re.sub("shankha",           ")*(100000000000000000)+(0", x)
    x = re.sub("Y",                 "", x)
    x = re.sub(" ",                 "", x)
    x = re.sub("^",                 "(0", x)
    x = re.sub("$",                 ")", x)
    x = re.sub("\(0\(",             "", x )
    x = re.sub("\+\+",              "\+\(", x )
    x = re.sub("\)\+\)",            "\)", x )
      
    y = int(eval(x))
    return(y)
