# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:14:34 2018

@author: SBOHORA
"""

a = 0
b = 1

for i in range(0,10):
    print(a)
    a, b = b, a + b
    #a = b
    #a,b = b, a + bR
    
my_dict = {'name': 'Bronx', 'age':2,'Occupation':'Statistician'}

for key, val in my_dict.items():
    print("My " + key + " is " + str(val))
    print("My {} is {}".format(key, val))
    
    
class Restaurant(object):
    bankrupt = False
    def open_branch(self): # this is same as this in C# and Java, self is not a reserved word
        if not self.bankrupt:
            print("branch opened")
            
            
x = Restaurant()
x.bankrupt = True
x.open_branch()
