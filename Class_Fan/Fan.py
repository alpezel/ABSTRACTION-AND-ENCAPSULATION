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

    # Speed
    def get_speed(self):
        return self.__speed
    def set_speed(self):
        return self.__speed
    
    # Radius
    def get_radius(self):
        return self.__radius
    def set_radius(self):
        return self.__radius
    
    # Color
    def get_color(self):
        return self.__color
    def set_color(self):
        return self.__color
    
    # On Fan
    def fan_on(self):
        return self.__on
    def set_on(self, on):
        self.__on = on


    

# testing
fan1= Fan(speed=Fan.fast, radius=10, color="yellow", on=True)
print("fan 1 test")
print("Speed:",fan1.get_speed())
print("Radius:",fan1.get_radius())
print("Color:",fan1.get_color())
print("Fan On:",fan1.fan_on())