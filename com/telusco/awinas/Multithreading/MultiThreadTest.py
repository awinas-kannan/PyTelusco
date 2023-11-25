from threading import *
from time import sleep


class Hi(Thread):
    def run(self):
        for i in range(1, 5):
            sleep(0.1)
            print(f"Hi {i}")


class Hello(Thread):
    def run(self):
        for i in range(1, 5):
            sleep(0.1)
            print(f"Hello {i}")


h1 = Hi()
sleep(1)
h2 = Hello()

h1.start()
h2.start()

h1.join()
h2.join()

print("Byeeee")