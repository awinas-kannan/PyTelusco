# defining car class
class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]


# creating objects of car class
audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)

print("############ ############### ##################")


# defining car class
class kwcar():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['speed']
        self.color = kwargs['clr']


# creating objects of car class
audi = kwcar(speed=200, clr='red')
bmw = kwcar(speed=250, clr='black')
mb = kwcar(speed=190, clr='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)
