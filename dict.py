#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Dictionary - key: value

d = {key1 : value1, key2 : value2 }

"""

def main():
    dict = {'Alice':53,'Lisa':22,'Bob':33,'Alex':'Hi'}
    print("dict[Alice]:",dict['Alice'])
    for elem in dict:
        print(elem, dict[elem])
    dict['Lisa'] = 18
    dict['School'] = "UNSW"
    dict.update(Bob=29)
    print("Bob:",dict['Bob'])
    print(dict.popitem())
    # delte Alex item
    dict.pop('Alex','Hi')
    print(dict)
    print(dict.keys())
    print(dict.values())

if __name__ == '__main__':
    main()