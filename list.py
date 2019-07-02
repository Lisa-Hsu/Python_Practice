#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
list 
"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()

    fruit2 = fruits[2:6]
    print(fruit2)

    fruit3 = fruits
    print(fruit3)

    fruit4 = fruits[-4:-1]
    print(fruit4)

    fruit5 = fruits[::-1]
    print(fruit5)

    #sorted() copy一份列表排序後傳回
    list1 = sorted(fruits)
    print(list1)

    #sort() 直接在list上進行排序 
    fruits.sort(reverse=True)
    print(fruits)

    list2 = fruits
    print(list2)

    #依據字串長度進行排序
    list3 = sorted(fruits,key=len)
    print(list3)

def main2():
    import sys
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    f = [x ** 2 for x in range(1, 100)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)

    #使用generator(生成器)
    f = (x ** 2 for x in range(1, 100))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val,end=' ')
    print()

if __name__ in "__main__":
    main()
    main2()
