#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Dictionary - key: value

d = {key1 : value1, key2 : value2 }

"""
import time
import os

class Clock(object):

    def __init__(self, hour=0 , minute=0 , second=0 ):
        self._hour = hour
        self._minute = minute
        self._second = second

    def show(self):
        return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
        
def main():
    clock = Clock(22,5,30)
    while True:
        os.system('clear')
        print(clock.show())
        time.sleep (1)
        clock.run()


if __name__ == "__main__":
    main()