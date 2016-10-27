# -*- coding: utf-8 -*-
"""
Simply study related to  static and class methods

"""
import datetime


# First Example

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
        
# Second Example

class Monster(object):
    
    
    # delta position - class variable
    delta_position = 10
    #number of monters
    num_of_monsters = 0
    
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        
        Monster.num_of_monsters+=1
        
    def move(self, posx,posy):
        self.posx = posx+ self.delta_position
        self.posy = posy +self.delta_position
        
    def position(self):
        return '{} , {}' .format(self.posx,self.posy)
     
    # used to change the value of class variable
    # same as Monster.delta_position = new_value
    @classmethod
    def set_move(cls,inc):
        cls.delta_position = inc

    #using classmethod as alternatives consctructor
    @classmethod
    def from_str(cls,pos_str):
        posx, posy = pos_str.split("-")
        return cls(posx,posy)      
       
    #static methods
    #behaves like a regular function
    @staticmethod
    def is_gameday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True
            
        
        
if __name__ == "__main__":
    
    # First Example
    
    # declare an instance of Warrior Class
    Savage = Warrior(20,10)
    Savage.move(10,25)
    print(Savage.position())
    
    # print namespace of instance
    print (Savage.__dict__)
    
    # print namespace of class Warrior
    print (Warrior.__dict__)
    # print number of objects
    print (Warrior.num_of_warriors)
    
    # Second Example
    
    monster = Monster(30,20)
    print(monster.position())
    # change value of class variable
    Monster.set_move(5)
    monster.move(10,10)
    print(monster.position())
    
    # using the "alternative constructor"
    second_monster = Monster.from_str("10-30")
    print(second_monster.__dict__)
    
    # to test staticmethod
    now = datetime.datetime.now()
    print (Monster.is_gameday(now))
    
    
    