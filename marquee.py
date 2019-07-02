#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
marquee
"""

import os
import time


def main():
    content = ' Hello , I am Lisa. It\'s a great day! '
    while True:
        # 清理屏幕上的输出
        #os.system('cls')  
        #for python3
        os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()