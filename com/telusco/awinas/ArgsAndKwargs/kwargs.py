print("************************* (*kwargs)")


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s %s" % (key, value, "HI"))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


def myFun1(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s %s" % (key, value, arg1))


# Driver code
myFun1("Hi", first='Geeks', mid='for', last='Geeks')
