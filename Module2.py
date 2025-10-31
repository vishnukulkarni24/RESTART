def func2():
    print("We are in the module 2")


def SecondFunc(x):
    if type(x) == str:
        print(x.upper())
    elif type(x) == int or type(x) == float:
        print(x+500)
    else:
        print(x)


def PrintRes(a,b):
    print(f"The result of addition = {a}")
    print(f"The result of multiplication = {b}")