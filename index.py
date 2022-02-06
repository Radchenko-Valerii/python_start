from math import *

a = "abc sda"
a.upper().capitalize()
print(a.index("sda"))

b = -6.7
print(abs(floor(b)))

num1 = float(input("enter the number: "))
num2 = float(input("enter second number: "))
print("~", floor(num1 + num2))

dmn = ["ad", "da", "net", "daa"]
print(dmn[1:3])

arr = ['a', 'b', 'c']
arr2 = arr.copy()
arr.pop()
print(arr2, arr)

b = (['as'], ('asda', 12, 'asdsadasdasd', arr), [6, 8, 9, 120])
print(b)

# ggg: str = "sdas"
# ggg = ("ssad","adsa")
# print(ggg)

obj = {
    'a': 'aaa',
    'b': 'bbb',
    'c': 'ccc'
}
print(obj['c'])
print(obj.get('d', 'not exists'))

oo = 'Aaa'
print(oo.lower())
print(oo)
