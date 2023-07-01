# Import class car
from Car import Car
boarder = "\n\033[0;39m===================================================\n"
def TestCar():
    car1 = Car(2020,"Honda")
    
    # Display Car's Model and Make
    print(boarder)
    print("Car Year Model and Make:","\n\033[0;34m",car1.get_year_model(),car1.get_make(),"\n\033[0;39m")
    print(boarder)

    # Call accelerate method 5 times
    for i in range(5):
        car1.accelerate()
        print("Current Speed:","\033[0;42m",car1.get_speed(),"Kph","\033[0;39m")

    # Call brake method 5 times
    for i in range(5):
        car1.brake()
        print("Current Speed:","\033[0;41m",car1.get_speed(),"Kph","\033[0;39m")
    print(boarder)
    
TestCar()