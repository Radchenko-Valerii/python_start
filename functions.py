from datetime import *

def wining_func():
    print("You win")

def loosing_func():
    print("You loooooooose")

def power(a: int, b: int):
    return a**b

def loto_ticket():
    ticket = float(input("Enter the number from 1 to 10: "))
    if ((datetime.today() - datetime(1970,1,1)).seconds)%ticket == 0:
        return (wining_func())
    else:
        return (loosing_func())
#     я знаю что это дичь и что тут разные вероятности в зависимости от числа 10 - 0%, 1 - 100%

loto_ticket()
