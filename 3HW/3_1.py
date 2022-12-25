# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).


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
        a.append (randint(-100,100))
    print(a)
    return a

def Count (a):
    asum = 0
    for i in range(0,(len(a)),2):
        asum += a[i]
    return asum


print(f'Sum of odd positioned nums is {Count(UserList())}')



