class A:

    def __init__(self):
        print("Inside Init A")

    def feature1(self):
        print("feature1")

    def feature2(self):
        print("feature2")


class B(A):

    def __init__(self):
        super().__init__()
        print("Inside Init B")

    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature4")


a1 = A()
b1 = B()

b1.feature1()
