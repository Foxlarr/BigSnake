#prog to check if one numbe = ^2 of the second

n = int(input())
m = int(input())

if n == m ** 2 or m == n ** 2:
    print('yes')
else:
    print('no')