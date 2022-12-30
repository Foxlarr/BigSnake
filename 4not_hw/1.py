# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

def check ():
    enlist = input('enter string').split()
    thelist = []
    for i in range (len(enlist)):
        enlist[i] = enlist[i].strip('!,;.')
        if enlist[i].isdigit:
            thelist.append(enlist[i])
    print(thelist)
    return thelist

def max_min (a):
    if a:
        return max(a,key=int), min(a,key=int)
    return []

print (max_min(check()))


