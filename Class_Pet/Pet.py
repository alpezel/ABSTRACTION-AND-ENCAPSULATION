# Make a class Pet
class Pet:
    def __init__(self,name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # Add Getter/Setter Methods

    # Name
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    # Animal Type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def get_animal_type(self):
        return self.__animal_type
    
    
    # Age
    def set_age(self,age):
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    