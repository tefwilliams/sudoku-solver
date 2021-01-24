# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:24:24 2020

@author: tefwi
"""


class SolveError(Exception):
    def __init__(self, message):
        self.message = message