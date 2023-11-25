class PyCharm:
    def execute(self):
        print("Compiling in pycharm")
        print("Building in pycharm")


class Jupiter:
    def execute(self):
        print("Compiling in Jupiter")
        print("Building in Jupiter")


class Laptop:
    def code(self, ide):
        ide.execute()


py = PyCharm()
ju = Jupiter()

l1 = Laptop()
l2 = Laptop()

l1.code(py)
l2.code(ju)
