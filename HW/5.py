# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Enter a coordinate along the axis {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Numbers please")
    return a


def calculating(a, b):
    length = ((b[0]-a[0])**2+(b[1]-a[1])**2)**(0.5)
    return length


print("Enter A point")
pointA = inputNumbers(2)
print("Enter B point")
pointB = inputNumbers(2)

print(f"Length is: {format(calculating(pointA, pointB), '.2f')}")
