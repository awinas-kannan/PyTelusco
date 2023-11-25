def topTen():
    yield 100


def topThreeRange():
    yield 1
    yield 3
    yield 5


def top10PerfectSq():
    n = 1
    while n < 10:
        print("yielding")
        sq = n * n
        yield sq
        n = n + 1


val = topTen()

print(val.__next__())
# print(val.__next__())

val = topThreeRange()

print(val.__next__())

for x in val:
    print("in loop")
    print(x)

print("------------------------")
val = top10PerfectSq()

for x in val:
    print(x)
