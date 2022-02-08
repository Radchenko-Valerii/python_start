# while True:
#     y = 1
#     i = 0
#     var = float(input('введите число '))
#     while i < var:
#         i += 1
#         y *= i
#
#     else:
#         print(y)
#



# def reverseFive(words):
#     resc = words.split()
#     result = []
#     for word in resc:
#         if len(word) > 4:
#             result.append(word[::-1])
#         else:
#             result.append(word)
#     return(' '.join(result))
#
# reverseFive('asdim')

def max(num):
    res = []
    for n in str(num):
        res.append(n)

    res.sort(reverse=True)
    return int(''.join(res))


print(max(123))


