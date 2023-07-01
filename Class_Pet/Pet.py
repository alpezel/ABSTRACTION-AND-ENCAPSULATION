# Make a class Pet
class Pet:
    def __init__(self,name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # Add Getter/Setter Methods

    # Name
    def get_name(self):
        return self.__name
    def set_name(self):
        return self.__name
    
    # Animal Type
    def get_animal_type(self):
        return self.__animal_type
    def set_animal_type(self):
        return self.__animal_type
    
    # Age
    def get_age(self):
        return self.__age
    def set_age(self):
        return self.__age
    