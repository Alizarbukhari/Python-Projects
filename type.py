from enum import Enum

# Define an enumeration class

class gender(Enum):
    male = str
    female  = str 
class students ():
    def __init__(self, id:int ,name:str ,age:int,grade:str):
        self.id = id
        self.name = name
        self.age = age
        self.grade= grade