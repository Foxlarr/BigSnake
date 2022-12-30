# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.


from random import randint
from random import choice
with open('poly1.txt', 'a', encoding='utf-8') as Afile:
    k = int(input('Введите натуральную степень k:'))
    a2 = ["+","-"]    
    for i in range (randint(3,5)):
        Afile.write ('\n')
        for i in range (k,0,-1):
            Afile.write (f"{randint(0,10)}*X^{i}")
            if i > 1:
                Afile.write (f' {choice(a2)} ')
            else:
                Afile.write (' = Y')



# def xfiles ():
#     for i in range (2):
#         with open(f'poly{i}.txt', 'a', encoding='utf-8') as Afile:
#             k = int(input('Введите натуральную степень k:'))
#             a2 = ["+","-"]    
#             for i in range (randint(3,3)):
#                 Afile.write ('\n')
#                 for i in range (k,0,-1):
#                     Afile.write (f"{randint(0,10)}*X^{i}")
#                     if i > 1:
#                         Afile.write (f' {choice(a2)} ')
#                     else:
#                         Afile.write (' = Y')
