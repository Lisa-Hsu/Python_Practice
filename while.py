"""
guess number
"""
import random

ans = random.randint(1,100)
counter = 0

while True:
    counter += 1
    num = int(input('input a num:'))
    if num < ans:
        print('bigger')
    elif num > ans:
        print('smaller')
    else:
        print('bingo')
        break

print('counter:',counter)

