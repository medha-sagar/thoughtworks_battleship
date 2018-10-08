# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:52:26 2018

@author: I335773
"""
class coordinates:
    def get_coordinates(pos):
        try:
            x = int(ALPHA_NUM.alphaToNum(pos[0]))-1
            y = int(pos[1])-1
        except:
            raise ValueError
        return x, y     
