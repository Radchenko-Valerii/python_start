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

loto_ticket()
