# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 04:20:51 2018

@author: I335773
"""
from alpha_num import Alpha_Num
from validation import *

ALPHA_NUM = Alpha_Num()

def set_ship_positions(ship, battleground):
    batship_type, batship_w, batship_h, pos = ship.batship_type, ship.batship_w, ship.batship_h, ship.position
    x, y = get_coordinates(pos)
    for i in range(batship_h):
        for j in range(batship_w):
            try:
                if battleground[x+i][y+j] == 0:
                    if batship_type.upper() == 'Q':
                        battleground[x+i][y+j] = 2
                    elif batship_type.upper() == 'P':
                        battleground[x+i][y+j] = 1
                else:
                    raise InvalidShipCoordinates
            except:
                raise IndexError
				
def get_coordinates(pos):
    try:
        x = int(ALPHA_NUM.alphaToNum(pos[0]))-1
        y = int(pos[1])-1
    except:
        raise ValueError
    return x, y    
