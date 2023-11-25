import this


class NewComp:

    def __init__(self, core, ram, rom):
        self.core = core
        self.ram = ram
        self.rom = rom

    def config(self):
        print(f"This computer config is {self.core} {self.ram} GB {self.rom} GB")

    def compare(self, other):
        if self.core == other.core and self.rom == other.rom and self.ram == other.ram:
            print(self, other, 'Are same')
            return None
        print(self, other, 'Are Not same')


c1 = NewComp("i5", 16, 512)
c1.config()
c2 = NewComp("i10", 16, 512)
c2.config()
c3 = NewComp("i10", 16, 512)
c3.config()
print(id(c1))
print(id(c2))
print(c3 == c2)
c1.compare(c2)
c2.compare(c3)
print(c1.__eq__(c2))
