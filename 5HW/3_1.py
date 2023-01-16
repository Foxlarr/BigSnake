# Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба


a = input("Enter text with spaces\n")
print(f"Text:  {a}")
target = "абв"
a2 = [i for i in a.split() if target not in i]
print('Words with "абв" has been remowed')
print(f'Result: {" ".join(a2)}')
