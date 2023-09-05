# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:15:18 2020

@author: tefwilliams
"""


class Cell:
    was_changed = False

    def __init__(self, value: int, coords: tuple[int, int]):
        self.value = value
        self.coords = coords
        self.potential_values: list[int] = ([] if self.is_solved() else [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def is_solved(self) -> bool:
        return self.value != 0

    def has_no_potential_values(self) -> bool:
        return len(self.potential_values) == 0
    
    def set_value(self, value: int) -> None: 
        self.potential_values.remove(value)
        self.value = value

    def is_wrong(self, grid) -> bool:
        return ((not self.is_solved() and self.has_no_potential_values())
            or (self.is_solved() and not grid.possible(self.coords, self.value)))

