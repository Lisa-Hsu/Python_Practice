#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
element
"""

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print("set1:",set1)
    print("set2:",set2)
    #如果元素不存在，不会发生错误
    set2.discard(5)
    print("set2:",set2)   
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print("set2:",set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    ele = set3.pop()
    print("ele:",ele)
    print(set3)
    print(set3.pop())
    print(set3)
    # 集合的交集、并集、差集、对称差运算
    print("and:",set1 & set2)
    # print(set1.intersection(set2))
    print("or:",set1 | set2)
    # print(set1.union(set2))
    print("diff:",set1 - set2)
    #print(set1.difference(set2))
    print("diff:",set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ in "__main__":
    main()
