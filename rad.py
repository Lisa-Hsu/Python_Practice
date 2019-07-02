#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
random a number to show verification code.
"""
import random

def generate_code(code_len):
    #all_chr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    all_chr = [x for x in range(0,10)]
    all_chr.extend([chr(i) for i in range(ord('a'), ord('z') + 1)])
    all_chr.extend([chr(i) for i in range(ord('A'), ord('Z') + 1)])
    leng = len(all_chr)-1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,leng)
        code += str(all_chr[index])
    return code


def main():
    number = int(input('Enter a number:'))
    print(generate_code(number))


if __name__ == '__main__':
    main()