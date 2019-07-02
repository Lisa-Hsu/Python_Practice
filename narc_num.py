#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Narcissistic number
每個位數的位數次方()和等於本身
1^3 + 5^3+ 3^3 = 153
1^4 + 6^4 + 3^4 + 4^4 = 1634
"""
import math

border = int(input('please enter a range:')) 
num = 0
sum_num = 0
middle = 0
for num in range(0, border):
    nn = str(num)
    length = len(str(nn))
    for i in range(0, length):
        sum_num += int(nn[i])**length
    if sum_num == num :
        print("%d is Narcissistic number" % num)
    sum_num = 0
    num += 1


