class Student:
    school = 'velammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'Hp'
            self.ram = '16 GB'

        def show(self):
            print(self.brand, self.ram)


s1 = Student("Awinas", 20)
s2 = Student("Kannan", 23)

s1.show()

##Both will have diff ids
print(id(s1.lap))
print(id(s2.lap))

# Create Laptop Obj

lap1 = Student.Laptop()
lap2 = Student.Laptop()
lap1.show()
