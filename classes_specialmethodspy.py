# -*- coding: utf-8 -*-
"""
Simple study related do classes magic methods - "dunders"

"""

# General Class

class Warrior(object):
    
    # delta position - class variable
    delta_position = 10
    #number of warriors
    num_of_warriors = 0
    
    
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        
        Warrior.num_of_warriors+=1
         
    def move(self, posx,posy):
        self.posx = posx+ self.delta_position
        self.posy = posy +self.delta_position
        
    def position(self):
        return '{} , {}' .format(self.posx,self.posy)
         
    # should be able ro recreate the object
    def __repr__(self):
        return "Warrior('{}','{}')".format(self.posx,self.posy)
    
    # 
    def __str__(self):
        return "'{}'-'{}'".format(self.posx,self.posy)


if __name__ =="__main__":
    
    warrior = Warrior(10,20)
    print(warrior.__repr__())
    print(warrior.__str__())