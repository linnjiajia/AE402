# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:39:01 2020

@author: linn2
"""

class Animal:
    def __init__(self,HP):
        self.HP = HP
    def hurt(self, demage):
        self.HP -= demage
        print("剩下血量:" + str(self.HP))
        
class Dog(Animal):
    def __init__(self,HP):
        super().__init__(HP)
        
    def howl(self):
        print("汪汪汪")
        
        
class ShibaInu(Dog):
    def __init__(self):
        super().__init__(1)
    
    def howl(self):
        print("阿囉哈")
        
class WelshCorgi(Dog):
    def __init__(self):
        super().__init__(1)
        
    def howl(self):
        print("呱呱呱")
        
a = WelshCorgi()
        
    


       
        
        
        
        
        
        
        
        
        
        
        