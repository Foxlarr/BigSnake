#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 

def Fibonacchi (n):
    a = [0,1,1]
    for i in range (3,n):
        a.append (a[i-1]+a[i-2])
    return a

def NFibonacchi (n):
    b = [-1,1,0]
    for i in range (-4,-(n+1),-1):
        b.insert (0,b[i+2]-b[i+1])
    return b
   
def Merge(a,b):
    a.pop(0)
    b.extend(a)
    return b

n = int(input())
a = (Fibonacchi(n))
b = (NFibonacchi(n))

print(Merge(a,b))































# WHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT.
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)


# a = [1,1,2,int(input('enter len '))]
# for i in range (3,len(a)):
#     a.append(fibonacci(i+1))
# print(a)

# print(fibonacci(4))