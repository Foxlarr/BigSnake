# Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.



def print_line():
    print("-" * 13)

def print_tab(tab):
    print_line()
    for i in range(3):
        print ("|", tab[0+i*3], "|", tab[1+i*3], "|", tab[2+i*3], "|")
        print_line()

def input_data(player_token, tab):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(tab[player_answer-1]) not in "XO"):
                tab[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")

def check(tab):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if tab[each[0]] == tab[each[1]] == tab[each[2]]:
            return tab[each[0]]
    return False

# from print_tab import print_tab as pt
# from input_data import input_data
# from check import check


def main(tab):
    counter = 0
    win = False
    while not win:
        print_tab(tab)
        if counter % 2 == 0:
            input_data("X", tab)
        else:
            input_data("O", tab)
        counter += 1
        if counter > 4:
            tmp = check(tab)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    print("Итоговая таблица:")
    print_tab(tab)


tab = list(range(1,20))

main(tab)