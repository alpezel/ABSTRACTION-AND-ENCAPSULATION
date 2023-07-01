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
InputPet()
