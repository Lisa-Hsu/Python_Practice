#!/usr/bin/python
# -*- coding: utf-8 -*-
#質因數分解

import math
import time
from prime_num import prime

def fun(x):
    print('{} = '.format(x),end='')
    if x <= 0 or not isinstance(x,int):
        print('is not a number')
        exit(0)
    elif x in [1]:
        print('{}'.format(x))
    while x not in [1]:
        for index in range(2,x+1):
            if (x % index == 0):
                x = (int)(x / index)
                if x == 1:
                    print(index)
                else:
                    print('{} * '.format(index),end='')
                break    


if __name__ == '__main__':
    a = eval(input("Enter a number:"))
    tstart = time.time()
    fun(a)
    tend = time.time()
    print('total time:{}'.format(tend-tstart))


