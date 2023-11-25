class A:

    def __init__(self):
        print("Inside Init A")

    def feature1(self):
        print("feature1")

    def feature2(self):
        print("feature2")

    def featureCommon(self):
        print("featureCommon A")


class B:

    def __init__(self):
        print("Inside Init B")

    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature4")

    def featureCommon(self):
        print("featureCommon B")


class C(A, B):
    pass


a1 = A()
b1 = B()
c1 = C()
c1.feature1()
c1.featureCommon()
