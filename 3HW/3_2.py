#   Напишите программу, которая найдёт произведение пар чисел списка.
#   Парой считаем первый и последний элемент, второй и предпоследний и т.д.

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
    from random import randint
    for i in range(f):
    #     a.append (randint(x,y))
        a.append (randint(0,10))
    print(a)
    return a

def Count (a):
    mult = []
    if (len(a)%2):
        a.insert(((len(a)//2)+1),1)
        print(a)
    for i in range(int(len(a)/2)):
        mult.append (a[i]*a[-(i+1)])

    return mult


print(f'Result {Count(UserList())}')