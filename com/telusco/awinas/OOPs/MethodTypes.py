class Student:
    school = 'velammal'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        print(self.m1 + self.m2 + self.m3)

    @classmethod
    def getSchool(cls):
        print(cls.school)

    @staticmethod
    def info():
        print("Static")


    def __eq__(self, __o):
        return super().__eq__(__o)


s1 = Student(1, 3, 4)
s2 = Student(2, 3, 5)
s3 = Student(1, 5, 4)

s1.total()

# Student.total()
Student.getSchool()
Student.info()
print(Student.school)
print(s1.__eq__(s2))
