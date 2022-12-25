# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def UserList ():
    a = []
    ok = False
    while not ok:
        try:
            f = int(input('Enter length of the list  '))
            # x = int(input('Enter a random number representing "from"   '))
            # y = int(input('Enter a random number representing "to"   '))
            # if x <= y:
            ok = True
            # else:
            #     print(f'"From" must be less than "to", not {x} <= {y}')
        except TypeError:
            print('int number, please')    
    from random import uniform
    for i in range(f):
    #     a.append (uniform(x,y))
        a.append (uniform(0,10))
    print(a)
    return a

def Transmute (a):
    b = []
    for i in range (0,len(a)):
        b.append (a[i]-(float(int(a[i]))))
        b[i] = round(b[i],2)
    return b

def Search (b):
    numA = max(b)
    numB = min(b)
    num = numA-numB
    return round(num,2)

a = (Transmute(UserList()))
print(a)
print(Search(a))


