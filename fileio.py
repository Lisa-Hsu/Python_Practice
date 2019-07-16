#!/usr/bin/python
# -*- coding: utf-8 -*-

def readfileasline(name):
    f = open(name,mode='r')
    while True:
        line = f.readline()
        if not line:
            break
        print('{}'.format(line),end='')
    f.close()

def readfile(name):
    with open(name, 'r') as filehandle:  
        for line in filehandle:
            print('{}'.format(line),end='')

def read(name):
    stri=[]
    with open(name, 'r') as filehandle:  
        filecontent = filehandle.read()
        print('{}'.format(filecontent))


def writefile(name):
    f = open(name,mode='w',encoding='utf-8')
    for i in range(ord('a'), ord('z') + 1):
        f.write(chr(i))
    f.write('\n')
    for i in range(ord('A'), ord('Z') + 1):
        f.write(chr(i))
    f.write('\n')
    f.close()

if __name__ == '__main__':
    readfileasline('ipod.log')
    print("\n\n")
    readfile("ipod.log")
    print("\n\nmethod3:")
    read("ipod.log")