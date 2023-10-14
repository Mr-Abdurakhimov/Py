from colorama import Fore

nums_str = (int(j) for i in range(1, 20) for j in str(i) if i != 10)
start_field = [[next(nums_str) for j in range(9)] for i in range(3)]
temp_field = [i.copy() for i in start_field]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
my_dict = {j: i for i, j in enumerate(letters)}


def draw_field():
    print("-" * 45)
    for i in range(len(start_field)):
        for j in range(len(start_field[i])):
            print(Fore.LIGHTWHITE_EX, f" {start_field[i][j]} ", end="|") if temp_field[i][j] != 0 else (print(Fore.RED,
                                                                                                              f" {start_field[i][j]}",
                                                                                                              Fore.LIGHTWHITE_EX,
                                                                                                              end="|"))
        if len(temp_field[i]) < 9:
            print(" " * (48 - len(temp_field[i] * 5)) + f"{i + 1}")
        else:
            print(f"\t{i + 1}")
        print("-" * 45)
    print("  " + "    ".join(letters))


def check_field():
    for i in range(len(temp_field) - 1):
        for j in range(len(start_field[i]) - 1):
            if (temp_field[i][j] == temp_field[i + 1][j] or temp_field[i][j] + temp_field[i + 1][j] == 10 or \
                temp_field[i][j] == temp_field[i][j + 1] or temp_field[i][j] + temp_field[i][j + 1] == 10) and \
                    temp_field[i][j] != 0:
                return True
    for i in range(len(temp_field[-1]) - 1):
        if (temp_field[-1][i] == temp_field[-1][i + 1] or temp_field[-1][i] + temp_field[-1][i + 1] == 10) and \
                temp_field[-1][i] != 0:
            return True
    return False


def check_step(letter_num1, letter_num2):
    letter1 = letter_num1[0].lower()
    num1 = int(letter_num1[1]) - 1
    letter2 = letter_num2[0].lower()
    num2 = int(letter_num2[1]) - 1
    if temp_field[num1][my_dict[letter1]] == temp_field[num2][my_dict[letter2]] \
            or temp_field[num1][my_dict[letter1]] + temp_field[num2][my_dict[letter2]] == 10:
        temp_field[num1][my_dict[letter1]] = 0
        temp_field[num2][my_dict[letter2]] = 0
    else:
        print("Неверная пара координат, вы пропускаете ход")


def change_field():
    new_spisok = []
    lst_of_new_spisoks = []
    for i in temp_field:
        for j in i:
            if j != 0:
                if len(new_spisok) < 9:
                    new_spisok.append(j)
                else:
                    lst_of_new_spisoks.append(new_spisok)
                    new_spisok = []
                    new_spisok.append(j)
    for i in lst_of_new_spisoks:
        temp_field.append(i.copy())
        start_field.append(i.copy())
    if new_spisok:
        temp_field.append(new_spisok.copy())
        start_field.append(new_spisok.copy())


def check_for_end():
    for i in temp_field:
        for j in i:
            if j != 0:
                return True
    return False


if __name__ == "__main__":
    while check_for_end():
        while check_field():
            draw_field()
            coors = input("Введите две координаты: ").split()
            check_step(coors[0], coors[1])
        change_field()
