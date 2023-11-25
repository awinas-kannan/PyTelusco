print("************************* (*args)")


def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("Python program to illustrate *args with a first extra argument")


def myFun1(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')





