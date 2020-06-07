# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""


class Cell:
    def __init__(self, value, coords):
        self.value = value
        self.coords = coords
        self.potential_values = ([] if self.is_solved()
                                 else [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def is_solved(self):
        return self.value != 0

    def has_no_potential_values(self):
        return len(self.potential_values) == 0
