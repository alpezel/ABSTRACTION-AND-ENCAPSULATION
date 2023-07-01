# Import class Pet
from Pet import Pet
boarder = "\n\033[0;39m===================================================\n"

def InputPet():
    pet = Pet("", "", 0)

    # Ask user for pets details with error handling
    print(boarder)
    while True:
        try:
            name = input("\033[0;47mEnter the pet's name: ")
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
    
    # Setting the Pet's details using setter method
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    # Display pet's details
    print(boarder)
    print("Pet's Name:", pet.get_name())
    print("Animal Type:", pet.get_animal_type())
    print("Pet's Age:", pet.get_age())
    print(boarder)
InputPet()
