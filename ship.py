# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:52:26 2018

@author: I335773
"""
from board import Board


class Ship:
    
    def __init__(self, batship_type, batship_w, batship_h, position):
        self.batship_type = batship_type
        self.batship_w = batship_w
        self.batship_h = batship_h
        self.position = position
    
    @property
    def batship_type(self):
        return self.__batship_type
    
    @property
    def batship_w(self):
        return self.__batship_w
    
    @property
    def batship_h(self):
        return self.__batship_h
    
    @property
    def position(self):
        return self.__position
    
    @batship_type.setter
    def batship_type(self, batship_type):
        self.__batship_type = batship_type
            
    @batship_w.setter
    def batship_w(self, batship_w):
        self.__batship_w = batship_w
        
    @batship_h.setter
    def batship_h(self, batship_h):
        self.__batship_h = batship_h
    
    @position.setter
    def position(self, position):
        self.__position = position
        
#    @property
#    def condition(self):
#        s = self.__potential_physical + self.__potential_psychic
#        if s <= -1:
#           return "I feel miserable!"
#        elif s <= 0:
#           return "I feel bad!"
#        elif s <= 0.5:
#           return "Could be worse!"
#        elif s <= 1:
#           return "Seems to be okay!"
#        else:
#           return "Great!" 
#  
#if __name__ == "__main__":
#    x = Robot("Marvin", 1979, 0.2, 0.4 )
#    y = Robot("Caliban", 1993, -0.4, 0.3)
#    print(x.condition)
#    print(y.condition)
    
    
#    def checkShipDimensions(self, m,n):
#        if (m*n > width * height):
#            print("wrong dimensions") 