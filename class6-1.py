# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:05:25 2020

@author: linn2
"""

class Human:
    def __init__(self,h, w):
        self.h = h
        self.w = w
        
    def BMI(self):
        print(self.w / (self.h / 100) **2)
        
        
h = Human(148.9, 39)
h.BMI()
 
        
        
    
        
        
        
        
        
        