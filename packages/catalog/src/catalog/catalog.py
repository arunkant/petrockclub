from enum import Enum

# make a enum for all types of rocks
class RockType(Enum):
    igneous = 1
    sedimentary = 2
    metamorphic = 3

# make a class for rocks
class Rock:
    def __init__(self, name, rock_type):
        self.name = name
        self.rock_type = rock_type

    def __str__(self):
        return f"{self.name} is a {self.rock_type.name} rock"


    
