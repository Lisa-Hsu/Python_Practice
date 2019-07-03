#!/usr/bin/python
# -*- coding: utf-8 -*-
#完美數 所有正因數的和相加＝本身 6＝1＋2＋3 28 ＝ 1＋2＋4＋7＋14

import math
import time
from prime_num import prime

def factor(x):
    k = []
    s = 0
    for i in range(1,x):
        if(x % i == 0):
            if (i not in k):
                k.append(i)
                if(i > 1):
                    k.append((int)(x/i))
            else:
                break
    print('{} = {}'.format(x,k))
    for j in k:
        s = s + j
    if s == x:
        return True
   


if __name__ == '__main__':
    for a in range(2,101):
        if(factor(a) == True):
            print('{} '.format(a))



