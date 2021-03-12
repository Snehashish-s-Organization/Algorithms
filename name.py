# Made by Snehashish Lskar
# Made on 11-03-2021
# This is a sort algrithm that sorts ppl based on their names

import string
students = ['armaan', 'uday', 'ruhan', 'vidushi', 'aashi', 'ruhani',
            ' siddharth', 'sohamm',  'ananya J', 'shaurya',
            'ishan', 'anindita', 'niloufer', 'ovee', 'amrita',
            'kailash', 'vashist', 'prakriti', 'hia', 'anadya',
            'anavi', 'ahona',
            'sreehita', 'reyansh', 'ruchira', 'kabir', 'namit',
            'nitin', 'shiv', 'indira', 'raju', 'aadil', 'ananya S', 'pratham',
            'rishabh', 'aadhira', 'yajnesh', "snehashish"]
alpha = list(string.ascii_lowercase)
dict1 = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [], "l": [], "m": [
], "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], "y": [], "z": []}

#
for student in students:
    stu = list(student)
    for letter in alpha:
        if stu[0] == letter:
            for c, d in dict1.items():
                if letter == c:
                    try:
                        dict1[c].append(student)
                    except:
                        print("Error")
for x, y in dict1.items():
    y.append(" ")
    if y[0] == " ":
        pass
    elif y[1] != " ":
        print(f"ppls who's names starts with {x} are {y}")
