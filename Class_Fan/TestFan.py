# Import class Fan 
from Fan import Fan

def FanTest():
    Fan1= Fan(speed=Fan.fast, radius=10, color="yellow", on=True)
    Fan2= Fan(speed=Fan.medium, radius=5, color="blue", on=False)


    # Fan 2 Properties
    print("Fan 2")
    print("Speed:",Fan2.get_speed())
    print("Radius:",Fan2.get_radius())
    print("Color:",Fan2.get_color())
    print("Fan On:",Fan2.fan_on())

FanTest()


