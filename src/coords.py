# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""


class Coords(tuple[int, int]):
    def __init__(self, value: tuple[int, int]):
        self.col = value[0]
        self.row = value[1]
