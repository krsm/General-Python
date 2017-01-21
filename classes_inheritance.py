# -*- coding: utf-8 -*-
"""
Simple study related do classes inheritance - creating subclasses

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
        
 # First Example
       
class Archer(Warrior):
    pass
        
 # Second Example
class Horseman(Warrior):
    
    def __init__(self,posx,posy, attack):
    # use the constructor of class Warrior use of super
        super().__init__(posx, posy)
        self.attack = attack

        
        

if __name__ == "__main__":
    
    # First Example
    archer = Archer(100,10)
    print(archer.posx)
    # printing the Method resolution order
    #print(help(archer))

    """
    
    class Archer(Warrior)
 |  Method resolution order:
 |      Archer
 |      Warrior
 |      builtins.object
 |  
 |  Methods inherited from Warrior:
 |  
 |  __init__(self, posx, posy)
 |  
 |  move(self, posx, posy)
 |  
 |  position(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Warrior:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Warrior:
 |  
 |  delta_position = 10
 |  
 |  num_of_warriors = 1

    """    
     # Second Example
    horseman = Horseman(10,20,56)
    print(horseman.attack)
    
