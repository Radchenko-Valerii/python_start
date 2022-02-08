import os
import time as TIME


def search(name, time):
    if time == '':
        time=1
    list_item = []
    for adresses, dirs, files in os.walk('/home/user/Desktop'):
        for file in files:
            full = os.path.join(adresses, file)
            if name == file.split('.')[0] or ((TIME.time() - os.path.getctime(full)) < float(time)):
                list_item.append(full)
    return list_item

print(search(str(input('type the name of file or press enter to skip')),
             (input('type the time in sec after creating file(s))'))))
