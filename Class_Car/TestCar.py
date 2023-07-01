# Import class car
from Car import Car

def TestCar():
    car1 = Car(2020,"Honda")

    for i in range(5):
        car1.accelerate()
        print("Current Speed:",car1.get_speed())
TestCar()