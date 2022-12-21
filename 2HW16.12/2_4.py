# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

n = int(input("Enter value "))

a = [i for i in range(-n,n)]

ok = False
while not ok:
    try:
        x = a[int(input("1'st position "))-1]*a[int(input("2'nd position "))-1]
        ok = True
    except IndexError:
        (print('Please, use numbers in range ({n},-{n}) '))
    except ValueError:
        (print('Please, use int numbers'))

print(x)


