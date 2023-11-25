
class computer:
    def config(self):
        print("This compouter config is i5 32GB 256GB")


c1 = computer()
c1.config()
computer.config(c1)
print(type(c1))
