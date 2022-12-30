# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

def UserList ():
    a = []
    ok = False
    while not ok:
        try:
            f = int(input('Enter length of the list  '))
            # x = int(input('Enter a random number representing "from"   '))
            # y = int(input('Enter a random number representing "to"   '))
            # if x <= y:
            if f>0:
                ok = True
            else:
                print ("only positive num") 
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


def Magic (a):
    b = []
    for i in a:
       if a.count(i) == 1:
           b.append(i)
    return (b)


print(Magic(UserList()))







