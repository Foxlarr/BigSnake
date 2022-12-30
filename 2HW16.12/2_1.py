
n = float(input())
m = len(str(n))
if n < 0:
    n *= -1
num = n * 10 ** (m-1)

sum = 0
for i in range(m+2):
    x = num%10
    sum += int(x)
    num = num//10
print(sum)
