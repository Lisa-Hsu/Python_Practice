# prime number, enter a number of range , print the prime number of the range.
#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import time

def prime(x):
    print('{} '.format(x),end='')
    if x == 3 or x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        m = x % 6
        if m != 1 and m != 5:
            return False            
        else:
            for i in range(5,int(math.ceil(math.sqrt(x)))+1,6):
                if (x % i == 0) or (x % (i+2) == 0): # x % i: 6x + 5 -> 6(x + 1) - 1 -> 6x - 1, x % (i + 2): 6x + 1
                    return False
            return True

if __name__ == '__main__':
    a = eval(input("Enter a number:"))
    if prime(a) == True:
        print('{0} is prime number'.format(a))
    else:
        print('{0} is Composite number'.format(a))

