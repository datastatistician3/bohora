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


def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_0 = build_profile('albert', 'einstein',location='princeton')
user_1 = build_profile('marie', 'curie',location='paris', field='chemistry')
print(user_0)
print(user_1)


def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers','onions', 'extra cheese')

import snake_case

snake_case.snake_case("Hi______   _____ There hrllo")


lst=[10, 20, 30, 40, 50]

lst[-2:]

lst[1:4] = [15,45,46]

lst
x=4
y =6
print("v=",3,"cm :",x,",",y+4)

lst = [11,18,9,12,23,4,17]
lost = []
for idx in range(len(lst)):
    val = lst[idx]
    if val > 15:
        lost.append(val)
        lst[idx] = 15
print("modif:",lst,"-lost:",lost)

for idx,val in enumerate(lst):
    print(idx,val)
'c'*5

my_dict.items()

'so2m'.isalpha()

def swap_case(x):
    m = []
    for i in x:
        if i.islower():
            m.append(i.upper())
            mm = ''.join(m)
        else:
            m.append(i.lower())
            mm = ''.join(m)
    return mm

swap_case('HackerRank.com presents "Pythonist 2".')

s = 'GNCHCDCDC'
s.startswith('CDC')

def count_substring(string, sub_string):
    sum_count = 0
    for i in range(len(string)):
        if string.startswith(sub_string, i):
            add = 1
            sum_count += add
    return sum_count

count_substring(s, 'CDC')  


n = 24
if n % 2 is not 0:
    print("Weird")
elif n <=5 and n >= 2:
    print("Not Weird")
elif n <=20 and 6 >= 2:
    print("Weird")
else:
    print("Not Weird")
    
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}


n = 5
print("Not Werid" if not n%2 and (n in range(2,6) or n >20) else "Weird")

print("%s", "sdf")


print(''.join(map(str,list(range(1,n)))) + str(n))


for i in range(1, n + 1):
    print(i, end = '')
