# Import class car
from Car import Car

def TestCar():
    car1 = Car(2020,"Honda")
    
    print("Car Model:",car1.get_year_model())
    print("Cake Brand:",car1.get_maker())
    for i in range(5):
        car1.accelerate()
        print("Current Speed:",car1.get_speed())
TestCar()