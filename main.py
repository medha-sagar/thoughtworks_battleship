# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:37:45 2018

@author: Medha Sagar
"""
import unittest
import string
from board import Board
from alpha_num import Alpha_Num
from ship import Ship
from validation import BattleWidthOutOfRange, BattleHeightOutOfRange, InvalidShipTypeError, InvalidBattleshipNumber
from utils import set_ship_positions, get_coordinates
import tests

def main():
    BOARD_P1 = Board()
    BOARD_P2 = Board()
    ALPHA_NUM = Alpha_Num()
    
    try:
        input_file = open('input.txt', 'r')
        lines = input_file.readlines()
        line_counter = 0
    except:
        raise IOError
    
    #Start reading Input
    char_width, height = str(lines[line_counter]).strip("\n").split(" ")
    width = int(char_width)
    
    #Validate Battle Area
    if width not in range(1, 9):
        raise BattleWidthOutOfRange
    
    if height.upper() not in list(string.ascii_uppercase):
        raise BattleHeightOutOfRange
    
    #Create battlegrounds for players
    battlegroud_p1 = BOARD_P1.createBattleground(width, height)
    battlegroud_p2 = BOARD_P2.createBattleground(width, height)
    
    #Get number of BattleShips
    line_counter += 1
    num_batship = int(lines[line_counter])
    
    #Validate Battleships
    if num_batship not in range(1, (width*int(ALPHA_NUM.alphaToNum(height)))):
        raise InvalidBattleshipNumber
    
    #Set the player boards
    
    board_weight = 0
    for i in range(num_batship):
        line_counter += 1
        try:
            batship_type, batship_w, batship_h, p1_pos, p2_pos = str(lines[line_counter]).strip("\n").split(" ")
        except:
            raise EOFError
        #Compute total missiles required to hit all ships
        #Validate ship type
        if batship_type.upper() == 'Q':
            board_weight += 2*(int(batship_w) * int(batship_h))
        elif batship_type.upper() == 'P':
            board_weight += (int(batship_w) * int(batship_h))
        else:
            raise InvalidShipTypeError
    
        #Initialize ships
        ship_p1 = Ship(batship_type, int(batship_w), int(batship_h), p1_pos)
        ship_p2 = Ship(batship_type, int(batship_w), int(batship_h), p2_pos)
    
        #Set ships on player boards
        set_ship_positions(ship_p1, battlegroud_p1)
        set_ship_positions(ship_p2, battlegroud_p2)
    
    
    line_counter += 1
    try:
        p1_attack_array = str(lines[line_counter]).strip("\n").split(" ")
    except:
        raise EOFError
    
    line_counter += 1
    try:
        p2_attack_array = str(lines[line_counter]).strip("\n").split(" ")
    except:
        raise EOFError
    
    p1, p2, total_p1, total_p2 = 0, 0, board_weight, board_weight
    
    turn = "p1"
    
    game_in_progress = True
    
    while game_in_progress is True:
        if turn == "p1":
            if p1 < len(p1_attack_array):
                p1_attack_pos = p1_attack_array[p1]
                x, y = get_coordinates(p1_attack_pos)
                if battlegroud_p2[x][y] == 0:
                    print("Player-1 fires a missile with target {} which got miss".format(p1_attack_pos))
                    turn = "p2"
                else:
                    print("Player-1 fires a missile with target {} which got hit".format(p1_attack_pos))
                    battlegroud_p2[x][y] -= 1
                    total_p1 -= 1
                    turn = "p1"
                p1 += 1
                if total_p1 == 0:
                    print("Player1 won the battle")
                    break
            else:
                print("Player-1 no more missiles left to launch")
                turn = "p2"
    
        elif turn == "p2":
            if p2 < len(p2_attack_array):
                p2_attack_pos = p2_attack_array[p2]
                x, y = get_coordinates(p2_attack_pos)
                if battlegroud_p1[x][y] == 0:
                    print("Player-2 fires a missile with target {} which got miss".format(p2_attack_pos))
                    turn = "p1"
                else:
                    print("Player-2 fires a missile with target {} which got hit".format(p2_attack_pos))
                    battlegroud_p1[x][y] -= 1
                    total_p2 -= 1
                    turn = "p2"
                if total_p2 == 0:
                    print("Player-2 won the battle")
                    break
                p2 += 1
            else:
                print("Player-2 no more missiles left to launch")
                turn = "p1"
    
    if total_p1 > 0 and total_p2 > 0:
        print("Both players declare peace")

if __name__== "__main__":
    
    unittest.main()
    main()
