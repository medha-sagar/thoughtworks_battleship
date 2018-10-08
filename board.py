# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:56:03 2018

@author: I335773
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:52:26 2018

@author: I335773
"""
from alpha_num import Alpha_Num

alpha_num = Alpha_Num()
class Board:
    def setBoardDim(self, x,y):
        self.__x = x
        self.__y = alpha_num.alphaToNum(y)
    
    def getBoardDim(self):
        return self.__x, self.__y
    
    def createBattleground(self, x, y):
        self.__battlegroud = [0] * alpha_num.alphaToNum(y)
        for i in range(alpha_num.alphaToNum(y)):
            self.__battlegroud[i] = [0] * x
        return self.__battlegroud