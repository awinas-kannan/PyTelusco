# from abc import *
from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

    def compute(self):
        print("Computing %s" % type(self).__name__)


class Laptop(Computer):

    def process(self):
        print("Processing laptop")


class Desktop(Computer):

    def process(self):
        print("Processing Desktop")


l1 = Laptop()
l1.process()

# c1 = Computer()
# c1.process()


l2 = Laptop()
d1 = Desktop()

l2.compute()
d1.compute()
