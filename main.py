from Module2 import *
from Module3 import add1
import Module1 as M1


val1 = 50
val2 = 5
a = add1(val1,val2)
b = M1.Mul(val1,val2)

def mainModule(value1,value2):
    PrintRes(value1,value2)
    print(add1(value1,value2))


mainModule(a,b)
mainModule(val1,val2)