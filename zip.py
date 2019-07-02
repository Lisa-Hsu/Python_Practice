# -*- coding: utf-8 -*-
#!/usr/bin/python
#zip and repeat
from itertools import repeat

a=[1,3,5,7]
b=[2,3,4,5]
print(list(zip(a,b)))
'''output
[(1, 2), (3, 3), (5, 4), (7, 5)]
'''
c=9
print(list(zip(a,repeat(c))))
'''output
[(1, 9), (3, 9), (5, 9), (7, 9)]
'''
d = [3.14,2.7183,0.009]
for i,j,k,l in zip(a,b,repeat(d),range(3)):
    print(i,j,k,l)
'''output
1 2 [3.14, 2.7183, 0.009] 0
3 3 [3.14, 2.7183, 0.009] 1
5 4 [3.14, 2.7183, 0.009] 2
'''
p=2
q=5
m=8
N=[0.111,0.314,11,33]
print("zip:",list(zip(repeat(p),repeat(q),range(len(N)),repeat(m),N)))
'''output
zip: [(2, 5, 0, 8, 0.111), (2, 5, 1, 8, 0.314), (2, 5, 2, 8, 11), (2, 5, 3, 8, 33)]
'''
print("zip1:",list(zip(repeat(p),repeat(q),range(len(N)),repeat(m),repeat(N))))
'''output
 [(2, 5, 0, 8, [0.111, 0.314, 11, 33]), 
 (2, 5, 1, 8, [0.111, 0.314, 11, 33]), 
 (2, 5, 2, 8, [0.111, 0.314, 11, 33]), 
 (2, 5, 3, 8, [0.111, 0.314, 11, 33])]
 '''