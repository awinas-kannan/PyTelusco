print(int.__add__(1, (4, 1)))
print(int.__add__(1, 10))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)

    def __gt__(self, other):
        return (self.m1 + self.m2) > (other.m1 + other.m2)

    def __str__(self):
        return "The Marks scores are %s %s " % (self.m1, self.m2)


s1 = Student(80, 60)
s2 = Student(60, 60)

s3 = s1 + s2
print(s3.m1, s3.m2)

s4 = s1.__add__(s2)
print(s4.m1, s4.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)
