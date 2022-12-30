# 3. На вход программе подается число n.
# Программа печатает численный треугольник.
# Используем вложенные циклы.


x = int(input('enter num \n'))
for i in range (1,x+1):
    for k in range (i):
        print(i, end='')
    print()