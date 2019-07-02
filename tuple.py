#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
tuple 
"""

def main():
    tu = ("lisa",33,True,"Taipei")
    print(tu)
    print(tu[0])
    print(tu[1])
    for member in tu:
        print(member)
    person = list(tu)
    person[0] = "Hello"
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    for x,y,z in ((2,3,4),(4,5,6),(7,8,9)):
        print(x+y+z)

if __name__ in "__main__":
    main()
