# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 03:39:09 2018

@author: I335773
"""

import unittest
import string
from board import Board
from alpha_num import Alpha_Num
from ship import Ship
from validation import *
from utils import set_ship_positions, get_coordinates

BOARD = Board()

ALPHA_NUM = Alpha_Num()


class TestExceptions(unittest.TestCase):
    
    def test_ship_width(self):
        input_file = open('input_test1.txt', 'r')
        lines = input_file.readlines()

        char_width = str(lines[0]).strip("\n").split(" ")[0]
        width = int(char_width)
        
        self.assertRaises(BattleWidthOutOfRange)
        
    def test_ship_height(self):
        input_file = open('input_test1.txt', 'r')
        lines = input_file.readlines()

        height = str(lines[0]).strip("\n").split(" ")
        
        self.assertRaises(BattleHeightOutOfRange)
        
    def test_ship_type(self):        
        input_file = open('input_test1.txt', 'r')
        lines = input_file.readlines()

        batship_type = str(lines[3]).strip("\n").split(" ")[1]
        
        if batship_type.upper() == 'Q':
            pass
        elif batship_type.upper() == 'P':
            pass
            
        self.assertRaises(InvalidShipTypeError)
        
    def test_ship_num(self):    
        input_file = open('input_test2.txt', 'r')
        lines = input_file.readlines()
        
        char_width, height = str(lines[0]).strip("\n").split(" ")
        width = int(char_width)
        
        num_batship = int(lines[1])
        
        self.assertRaises(InvalidBattleshipNumber)
        
    def test_ship_coordinates(self):    
        input_file = open('input_test2.txt', 'r')
        lines = input_file.readlines()
        
        char_width, height = str(lines[0]).strip("\n").split(" ")
        width = int(char_width)
        
        num_batship = int(lines[1])
        
        battlegroud = BOARD_P1.createBattleground(width, height)
        batship_type, batship_w, batship_h, p1_pos, p2_pos = str(lines[2]).strip("\n").split(" ")
        ship = Ship(batship_type, int(batship_w), int(batship_h), p1_pos)
        set_ship_positions(ship, battlegroud)
        
        self.assertRaises(InvalidShipCoordinates)
        
        
        
#    def test_IOError(self):
#        input_file = open('invalid_input.txt', 'r')
#        self.assertRaises(FileNotFoundError)
        
if __name__ == '__main__':
    unittest.main()