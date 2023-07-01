# Import class Fan 
from Fan import Fan
boarder = "\n\033[0;39m===================================================\n"
def FanTest():
    Fan1= Fan(speed=Fan.fast, radius=10, color="\033[0;43myellow\033[0;39m", on=True)
    Fan2= Fan(speed=Fan.medium, radius=5, color="\033[0;44mblue\033[0;39m", on=False)

    # Fan 1 Properties
    print(boarder)
    print("Fan 1:\n")
    print("Speed:",Fan1.get_speed())
    print("Radius:",Fan1.get_radius())
    print("Color:",Fan1.get_color())
    print("Fan On:","\033[0;42m",Fan1.fan_on(),"\033[0;39m")

    # Fan 2 Properties
    print(boarder)
    print("Fan 2:\n")
    print("Speed:",Fan2.get_speed())
    print("Radius:",Fan2.get_radius())
    print("Color:",Fan2.get_color())
    print("Fan On:","\033[0;41m",Fan2.fan_on(),"\033[0;39m")
    print(boarder)
FanTest()


