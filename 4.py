# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def inputCuarter():
    is_ok = False
    while not is_ok:
        try:
            number = int(input("Enter number of the quarter\n"))
            is_ok = True                          
        except ValueError:
                print("Please use only not float numbers") 

    return number

def correlateNumber(x):
    if x == 1:
        print(f"x > 0 and y > 0")
    elif x == 2:
        print(f"x < 0 and y > 0")
    elif x == 3:
        print(f"x < 0 and y < 0")
    elif x == 4:
        print(f"x > 0 and y < 0")
    else:
        print(f"There is no quarter with number {x}")

quarter = inputCuarter()
correlateNumber(quarter)