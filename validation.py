# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 01:24:59 2018

@author: I335773
"""

import string
from alpha_num import Alpha_Num
alpha_num = Alpha_Num()

class Error(Exception):
    pass

class BattleWidthOutOfRange(Error):
    pass

class BattleHeightOutOfRange(Error):
    pass

class InvalidShipTypeError(Error):
    pass

class InvalidBattleshipNumber(Error):
    pass

class InvalidShipCoordinates(Error):
    pass
