#  Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.



def shuffle (a):
    b = []
    from random import randint
    while len(b) != len(a):
        for i in range(len (a)):
            b.append(a[randint(0,(len(a)-1))])
        b = list(dict.fromkeys(b))
    return b

a = list(range(int(input())))
print(len(a))
print(f'{shuffle(a)} ')