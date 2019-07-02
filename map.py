# filter , map, reduce
# -*- coding: utf-8 -*-
names = ['Justin', 'caterpillar', 'openhome']
num = [1,2,3,4,5,6,7,8,9,10]
def fun(x):
    if len(x) > 6:
        return x
    else:
        return None

def p(x):
    return x*x

#python 3 filter/map is return Generator, use list to change type to list
#filter return boolean
b = list(filter(fun,names))
print(b) 
print(list(map(lambda ele: len(ele), names)))
print(list(map(p,num)))
