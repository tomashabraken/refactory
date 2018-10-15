# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:30:53 2018

@author: Beheerder
"""

# This is a version of snacknames (lesson 3) that is written poorly
# on purpose, so you can refactor it into something better
names = [
        ["Tinus"],
        ["Barrie"],
        ["Hans"]
        ]
#names.append("Tinus")
#names.append("Barrie")
#names.append("Hans")

#snacks = { 
#        "snack1" : "",
#       "snack2" : None,
#        "snack3" : 0
#}

for name in names:
    friend = name[0]
    print(f'{friend} is a name with the length of {str(len(friend))}')
    snack = input("What is your favorite snack?")
    name.append(snack)
    
for name in names:
    print(f'{name[0]} likes {name[1]}')
    
print(names)

"""
index = 0
while index < len(names):
    name = names[index]
    print(name)
    name_len = len(name)
    print(len(name))
    print("the length of " + name)

    if index == 0:
        snack1 = input("What is your favourite snack?")
    elif index == 1:
        snack2 = input("What is your favourite snack?")
    else:
        snack3 = input("What is your favourite snack?")

    index = index + 1

new_index = 0
for name in names:
    if new_index == 0:
        name1 = names[new_index]
        print(name + " likes " + snack1)

    if new_index == 1:
        name2 = names[new_index]
        print(name + " likes " + snack2)

    if new_index == 2:
        name3 = names[new_index]
        print(name + " likes " + snack3)

    new_index = new_index + 1

"""