# Import class Pet
from Pet import Pet
boarder = "\n\033[0;39m===================================================\n"

def InputPet():
    pet = Pet("", "", 0)

    # Ask user for pets details with error handling
    print(boarder)
    while True:
        try:
            name = input("\033[0;36mEnter the pet's name:\033[0;39m ")
            if not name:
                raise ValueError("\033[0;41mName should not be Empty\033[0;39m")
            break
        except ValueError as Error:
            print(Error)

    while True:
        try:
            animal_type = input("\033[0;36mEnter the type of animal:\033[0;39m ")
            if not animal_type:
                raise ValueError("\033[0;41mAnimal Type should not be Empty\033[0;39m")
            break
        except ValueError as Error:
            print(Error)
    
    while True:
        try:
            age = input("\033[0;36mEnter the pet's age:\033[0;39m ")
            age = int(age)
            if age <= 0:
                raise ValueError("\033[0;41mInvalid age. Please enter a valid positive integer age.\033[0;39m")
            break
        except ValueError as Error:
            print(Error)
    
    # Setting the Pet's details using setter method
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    # Display pet's details
    print(boarder)
    print("\033[0;36mPet's Name:\033[0;39m","\033[0;35m",pet.get_name(),"\033[0;39m")
    print("\033[0;36mAnimal Type:\033[0;39m","\033[0;35m",pet.get_animal_type(),"\033[0;39m")
    print("\033[0;36mPet's Age:\033[0;39m","\033[0;35m",pet.get_age(),"\033[0;39m")
    print(boarder)
InputPet()
