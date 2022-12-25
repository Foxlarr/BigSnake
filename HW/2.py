# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (De Morgan's law) not (A or B) = (not A) and (not B) statement cannot be false


def inputNum(num):
    xyz = ["W", "Z", "Y", "X"]
    a = []
    for i in range(num):
        a.append(input(f"Enter value {xyz[i]}: "))
    return a


def checkPredicate(x):
    LeftPart = not (x[0] or x[1] or x[2])
    RightPart = not x[0] and not x[1] and not x[2]
    result = LeftPart == RightPart
    return result


statement = inputNum(4)

if checkPredicate(statement) == True:
    print(f"The statement is true")
else:
    print(f"The statement is false")