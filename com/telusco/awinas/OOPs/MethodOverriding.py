class A:
    def show(self):
        print("Class A")


class B(A):
    pass


class C(B):
    def show(self):
        print("Class C")


c1 = C()
c1.show()

b1 = B()
b1.show()
