# # Напишите программу для проверки ложности утверждения (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

def inputNum(num):
    xyz = ["W", "Z", "Y", "X"]
    a = []
    for i in range(num):
        a.append(int(input(f"Enter value {xyz[i]}: ")))
    print (a)
    return a


def checkPredicate(x):
    result = (x[0] and x[1]) or not x[2] or (not x[3] == (not x[0]))
    print  (result)
    return result


statement = inputNum(4)

if checkPredicate(statement) == True:
    print(f"The statement is true")
else:
    print(f"The statement is false")

