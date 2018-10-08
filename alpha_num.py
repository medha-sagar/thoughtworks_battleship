# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:55:01 2018

@author: I335773
"""
import string 

class Alpha_Num:
    def alphaToNum(self, char):
        self.alpha_num_dict = dict(zip(string.ascii_uppercase, range(1,27)))
        return  self.alpha_num_dict[char.upper()]