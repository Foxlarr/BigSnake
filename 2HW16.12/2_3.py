# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input())
if n < 0:
    n *= -1
num_list = []
x = 0
y = 0
for i in range(n): 
    x = ((1+1/n)**n)
    num_list.append(x)
    y =+ x
print(num_list)
print (y)