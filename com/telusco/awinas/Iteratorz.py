list = [5, 25, 36, 31, 52, 51, 42]
for x in list:
    print(x)

it = iter(list)
print(it.__next__())
print(it.__next__())
print(next(it))

print("-----------------------")


class TopTen:

    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


tt = TopTen()

for x in tt:
    print(x)

print(next(tt, "Stopped"))

print(next(tt))

