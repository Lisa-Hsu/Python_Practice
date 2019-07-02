# -*- coding: utf-8 -*-
#property 
class screen(object):

    def __init__(self,width=0,height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise TypeError('source must be a interger!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
           raise TypeError('source must be a interger!')
        self._height = value


    @property
    def resolution(self):
        return self._height*self._width

s = screen()
s.height = 720
s.width = 1024
print(s.height)
print(s.resolution)
print(s.width)
s.height = 100
print(s.resolution)
    

    


    
