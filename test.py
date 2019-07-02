# filter , map, reduce
#!/usr/bin/python
# -*- coding: utf-8 -*-
def sum():
    total = 0
    for i in range(1,101):
        total = total + i
    return total

def odd():
    a=[]
    for i in range(101):
        if(i%2 != 0):
            a.append(i)
    print(a)

#sum of 1-2,3-4,5-6...99
def sum1():
    sum = 0
    x=range(1,99,2)
    y=range(2,99,2)
    for i,j in zip(x,y):
        sum = sum + (i-j)
    return sum

def fib(x):
    if x == 1:
        return [1]
    if x == 2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,x):
        fibs.append(fibs[-2]+fibs[-1])
    return fibs
        


if __name__ == '__main__':
    print("sum of 1 to 100:",sum())
    odd()
    print(sum1())
    print(fib(22))