# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:15:26 2022

@author: alejo
"""

class Dog:
    
    def __init__(self, bark):
        self.bark = bark
        
scooby = Dog("Woof")
print(scooby.bark)