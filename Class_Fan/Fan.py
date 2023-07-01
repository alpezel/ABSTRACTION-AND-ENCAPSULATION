# Make a class to represent a Fan
class Fan:
    slow= 1
    medium= 2
    fast= 3

    def __init__(self, speed=1, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Add Getter/Setter Methods
    def get_speed(self):
        return self.__speed
    def set_speed(self):
        return self.__speed
    

# testing
fan1= Fan(speed=Fan.fast, radius=10, color="yellow", on=True)
print("fan 1 test")
print("Speed:",fan1.get_speed())