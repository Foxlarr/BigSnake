#   Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

x = int(input('enter num: '))
a = []
ok = 0
while not ok:
    if x%2 == 0:
        x /= 2
        a.append(2)
    elif x%3 == 0:
        x /= 3
        a.append(3)
    elif x%5 == 0:
        x /= 5
        a.append(5)
    else:
        a.append(round(x))
        ok = 1
        if a[len(a)-1] == 1:
            a.pop(-1)
            

    
print(a)
