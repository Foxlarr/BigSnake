#Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N в виде списка.

n = int(input())
if n < 0:
    n *= -1
num_list = []
x = 1
for i in range(n): 
    x *= (i+1)
    num_list.append(x)
print (num_list)