# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

def inputCoordinates():
    a = [0] * 2
    is_ok = False
    for i in range(2):
        while not is_ok:
            try:
                number = float(input(f"Enter {i+1} coords "))
                a[i] = number
                is_ok = True                
                if a[i] == 0: 
                    is_ok = False                   
                    print("Coordinates cannot be 0")                
            except ValueError:
                print("Please use only numbers")                    
    return a

def correlateCoordinates(xy):
    if xy[0] > 0 and xy[1] > 0:
        print(f"The point is in the 1 quarter")
    elif xy[0] < 0 and xy[1] > 0:
        print(f"The point is in the 2 quarter")
    elif xy[0] < 0 and xy[1] < 0:
        print(f"The point is in the 3 quarter")
    elif xy[0] > 0 and xy[1] < 0:
        print(f"The point is in the 4 quarter")

Coordinates = inputCoordinates()
correlateCoordinates(Coordinates)

