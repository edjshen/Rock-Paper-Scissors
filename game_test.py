# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:10:41 2022

@author: edjsh
"""

from game import validate

def test_determination_of_the_winner():
    assert validate(0, 0) == 0 # represents a tie   
    assert validate(0, 1) == 2
    assert validate(0, 2) == 1

    assert validate(1, 0) == 1
    assert validate(1, 1) == 0 # represents a tie
    assert validate(1, 2) == 2

    assert validate(2, 0) == 2
    assert validate(2, 1) == 1
    assert validate(2, 2) == 0 # represents a tie
    

    
    