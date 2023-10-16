from colorama import Fore, init

init(autoreset=True)
field = [[" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "]]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
my_dict = {j: i for i, j in enumerate(letters)}
players = {1: "X", 2: "O"}
colors = {"X": Fore.LIGHTBLUE_EX, "O": Fore.LIGHTRED_EX}
res_1 = []
res_2 = []


def draw_field():
    print("\t\t\t\t\t\t\t\tБерег Ноликов")
    print("\t\t\t\t" + "-" * 41)
    for i, k in enumerate(field):
        if i == 4:
            print("Берег крестиков", end=" |")
            for j in k:
                print(f"\t{j}", end="")
            print(f"\t| {i + 1}", end="")
            print("   Берег крестиков")
        else:
            print("\t\t\t\t|", end="")
            for j in k:
                print(f"\t{j}", end="")
            print("\t|", i + 1)
    print("\t\t\t\t" + "-" * 41)
    print("\t\t\t\t\t", end="")
    print(("\t").join(letters))
    print()
    print("\t\t\t\t\t\t\t\tБерег ноликов")


def check_step(line, row, sign):
    if line - 1 >= 0 and line + 1 < 10:
        if field[line - 1][row] == sign and field[line + 1][row] == sign:
            field[line][row] = f"{colors[sign]}|"
            if sign == "X":
                res_1.append(row) if row not in res_1 else res_1
            else:
                res_2.append(line) if line not in res_2 else res_2
            return
    if row - 1 >= 0 and row + 1 < 10:
        if field[line][row - 1] == sign and field[line][row + 1] == sign:
            field[line][row] = f"{colors[sign]}--"
            if sign == "X":
                res_1.append(row) if row not in res_1 else res_1
            else:
                res_2.append(line) if line not in res_2 else res_2
            return
    print(f"Сюда нельзя ходить, потому что у {sign} нет пары, инициатива переходит сопернику")


def make_step(coor, player):
    sign = players[player]
    row = my_dict[coor[0].lower()]
    line = int(coor[1]) - 1
    if field[line][row] == " ":
        check_step(line, row, sign)
    else:
        print("К сожалению, вы сделали неправильный ход, инициатива переходит к сопернику")


def check_for_end():
    if 1 in res_1 and 3 in res_1 and 5 in res_1 and 7 in res_1:
        return True
    elif 1 in res_2 and 3 in res_2 and 5 in res_2 and 7 in res_2:
        return True
    return False


player = 1
while True:
    draw_field()
    step = input(f"Игрок {player}, сделайте ход: ")
    make_step(step, player)
    if check_for_end():
        break
    player = 2 if player == 1 else 1
draw_field()
print(f"Игрок {player} выиграл !!!")
