# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]


def UserList ():
    a = []
    ok = False
    while not ok:
        try:
            f = int(input('Enter length of the list  '))
            if f<0:              
                f = -f
                print (f"only positive num, lenght {-f} changed to length {f}") 
            ok = True

        except TypeError:
            print('int number, please')                

    for i in range(20,f+1):
        a.append (i)
 
    # print(a)
    return a

def magic(a):
    a2 = [i for i in a if not i%20 or not i%21]
    return a2

print(magic(UserList()))