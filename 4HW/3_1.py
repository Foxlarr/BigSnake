# Вычислить число c заданной точностью d

from decimal import Decimal

x = Decimal(input('enter a real number: '))
d = Decimal(input('enter the required accuracy: '))
print( x.quantize(d))