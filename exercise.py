#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Exercise - 
"""

def get_file_extension(filename):
    pos = filename.rfind('.')
    if 0 < pos < len(filename)-1:
        return filename[pos+1:]

def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    from random import randrange, randint, sample
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls



def main():
    # name = input("Enter filename:")
    # print(get_file_extension(name))
    display(random_select())

if __name__ == '__main__':
    main()
