# Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.



from random import randint
from random import choice

def xfiles ():
    for i in range (2):
        with open(f'poly{i}.txt', 'a', encoding='utf-8') as Afile:
            k = int(input('Введите натуральную степень k:'))
            a2 = ["+","-"]    
            for i in range (randint(3,4)):
                Afile.write ('\n')
                for i in range (k,0,-1):
                    Afile.write (f"{randint(0,10)}*X^{i}")
                    if i > 1:
                        Afile.write (f' {choice(a2)} ')
                    else:
                        Afile.write (' = Y')
def check():
    count1=0
    count2=0
    f = open("poly0.txt", "r")
    for x in f:
        count1+=1
    f = open("poly1.txt", "r")
    for x in f:
        count2+=1
    if not count1 == count2:
        return 0
    return 1


def merge ():    
    with open('poly0.txt', 'r',  encoding='utf-8') as text:
            for a in text:
                a = a.replace(' = Y', ' + hereberagon = Y')
                a = a.replace('-', '+')
                with open('poly1.txt', 'r',  encoding='utf-8') as text2:
                    for b in text2:
                        b = b.replace(' = Y', ' ')
                        b = b.replace('-', '+')
                a = a.replace('hereberagon',b)
                text3 = open('poly3.txt', 'a',encoding='utf-8')
                text3.write(a)


xfiles()
if not check():
    print('The contents of the files do not match!')
else:
    merge()

# def write (a):
    # with open ('poly3.txt', 'a', encoding='utf-8') as text3:
    #     while a:
    #         text3.write(a)

# write(merge)


































# def read (file):
#     with open(str(file), 'r') as data:
#         a1 = data.read
#     return a1

# print(read(file1))

# def transmute (a1):
#     a = a.replace(' = Y', ' hereberagon = Y')
#     a = 


# def merge ():

# with open('poly0.txt', 'r') as p1:
#     with open('poly1.txt', 'r') as p2:
#         for a in p1:
#             a = a.replace(' = Y', ' + hereberagon = Y')
#             a = a.replace('-', '+')
#             for b in p2:
#                 b = b.replace(' = Y', ' ')
#                 b = b.replace('-', '+')
#                 a = a.replace(' = Y', ' + hereberagon = Y')


#             # line.append(a.split('\n'))
#     print(a)
    
# with open('poly1.txt', 'r') as p2:
#     for b in p2:
#         b = b.replace(' = Y', ' ')
#         b = b.replace('-', '+')
#         print(b)

    

            
    