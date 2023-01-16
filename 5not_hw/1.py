# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.


def scroll(num):
    a = list(range(num+1))
    from random import choice
    a.remove(choice(a))
    return a

def magic(a):
    for i in range(1,len(a)):
        if not a[i] - 1 == a[i-1]:
            return a[i] - 1
    return -1


print(magic(scroll(int(input("Enter value: ")))))
