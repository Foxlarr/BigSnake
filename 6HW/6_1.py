# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

def UserList ():
    a = []
    ok = False
    while not ok:
        try:
            f = int(input('Enter length of the list  '))
            x = int(input('Enter a random number representing "from"   '))
            y = int(input('Enter a random number representing "to"   '))

            if f<0:              
                f = -f
                print (f"only positive num, lenght {-f} changed to length {f}") 

            if x <= y:
                ok = True
            else:
                print(f'"From" must be less than "to", not {x} <= {y}')
        except TypeError:
            print('int number, please')                
    from random import randint
    for i in range(f):
        a.append (randint(x,y))
        # a.append (randint(0,10))
    print(a)
    return a

# a = list(map(int,input("Enter numbers, separated by spaces: ").split()))

def scroll (a):
    
    a2 = [j for i, j in zip(a, a[1:]) if j>i]
    return a2

print(scroll(UserList()))