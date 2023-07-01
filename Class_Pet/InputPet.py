# Import class Pet
from Pet import Pet
boarder = "\n\033[0;39m===================================================\n"

def InputPet():
    pet = Pet("", "", 0)

    # Ask user for pets details with error handling
    while True:
        try:
            name = input("Enter the pet's name: ")
            if not name:
                raise ValueError("Name should not be Empty")
            break
        except ValueError as Error:
            print(Error)

    while True:
        try:
            animal_type = input("Enter the type of animal: ")
            if not animal_type:
                raise ValueError("Animal Type should not be Empty")
            break
        except ValueError as Error:
            print(Error)
    
    while True:
        try:
            age = input("Enter the pet's age: ")
            age = int(age)
            if age <= 0:
                raise ValueError("Invalid age. Please enter a valid positive integer age.")
            break
        except ValueError as Error:
            print(Error)
InputPet()
