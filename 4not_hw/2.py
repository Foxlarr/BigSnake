# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt
def find (a,b,c):
    D = (b**2 - 4*a*c)
    with open('Roots.txt', 'a', encoding='utf-8') as fileR:
        fileR.write(F'{a}x² + {b}x + {c} = 0\n')
        if D > 0:
            x1 = (-b-sqrt(D))/(2*a)
            x2 = (-b+sqrt(D))/(2*a)
            fileR.write(f'{x1,x2}\n')
        elif D == 0:
            x = -b/(2*a)
            fileR.write(f'{x}\n')
        else:
            fileR.write('no radicals\n')

find(3,8,2)