from random import randint

field = [[randint(1, 9) for i in range(3)] for j in range(3)]
player = 1
count_1 = 0
count_2 = 0
condition_1 = -1
condition_2 = 0


def draw_field():
    print("-" * 12, f"\tОчки игрока №1: {count_1}\tОчки игрока №2: {count_2}")
    for i in field:
        for j in i:
            print(f" {j} |", end="")
        print()
        print("-" * 12)

def end_game():
    if count_1 > count_2:
        print("Игрок 1 победил, у него больше очков")
    elif count_2 > count_1:
        print("Игрок 2 победил, у него больше очков")
    else:
        print("Ничья")

def make_a_step_p1(line, row):
    global count_1, condition_2
    try:
        count_1 += field[line][row]
        condition_2 = row
    except:
        print("Невозможно произвести действие, вы теряете ход")
        return
    field[line][row] = " "


def make_a_step_p2(line, row):
    global count_2, condition_1
    try:
        count_2 += field[line][row]
        condition_1 = line
    except:
        print("Невозможно произвести действие, вы теряете ход")
        return
    field[line][row] = " "


def check_condition1():
    okay = False
    for i in range(3):
        if type(field[condition_1][i]) is int:
            okay = True
    return okay


def check_condition2():
    okay = False
    for i in range(3):
        if type(field[i][condition_2]) is int:
            okay = True
    return okay

def game_on():
    okay = False
    for i in field:
        for j in i:
            if type(j) is int:
                okay = True
                return okay
    return okay

if __name__ == "__main__":
    print("Добро пожаловать в игру 'Маскит' ")
    while game_on():
        draw_field()
        if player == 1:
            print(f"Игрок № {player}, введите строку и столбец числа, которого хотите забрать. ")
            print(f"Ограничение на строку: {'нет' if condition_1 == -1 else condition_1 + 1}")
            step = [int(i) - 1 for i in input().split()]
            if condition_1 == -1:
                make_a_step_p1(step[0], step[1])
            else:
                if check_condition1():
                    if step[0] == condition_1:
                        make_a_step_p1(step[0], step[1])
                    else:
                        print("У вас есть ограничение на строку ! Введите координату заново")
                        continue
                else:
                    print("У вас нет клеточек для действия, ход переходит противнику")
                    player = 2
                    continue
            player = 2
        else:
            print(f"Игрок № {player}, введите строку и столбец числа, которого хотите забрать. ")
            print(f"Ограничение на столбец: {condition_2 + 1}")
            step = [int(i) - 1 for i in input().split()]
            if check_condition2():
                if step[1] == condition_2:
                    make_a_step_p2(step[0], step[1])
                else:
                    print("У вас есть ограничение на столбец ! Введите координату заново")
                    continue
            else:
                print("У вас нет клеточек для действия, ход переходит противнику")
                player = 1
                continue
            player = 1

    end_game()