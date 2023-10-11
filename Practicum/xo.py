field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
players = ["X", "О"]
game_on = True


def draw_field():
    print("-" * 12)
    for i in range(3):
        print("", field[i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-" * 12)


def shoot(num, cnt):
    if check_num(num):
        field[int(num)-1] = players[cnt]
        check_for_win()
        if cnt == 0:
            cnt += 1
        else:
            cnt = 0
        return cnt
    else:
        print("Неверное значение, введите ячейку заново")


def congratulate():
    draw_field()
    print(f"""Игрок, играющий за {players[count]} победил ! Поздравляем""")
    global game_on
    game_on = False


def check_num(num):
    if num.isdigit() and int(num) in field:
        return True
    else:
        return False


def check_for_win():

    if field[0] == field[1] == field[2]:
        congratulate()
    elif field[0] == field[3] == field[6]:
        congratulate()
    elif field[3] == field[4] == field[5]:
        congratulate()
    elif field[6] == field[7] == field[8]:
        congratulate()
    elif field[2] == field[5] == field[8]:
        congratulate()
    elif field[1] == field[4] == field[7]:
        congratulate()
    elif field[0] == field[4] == field[8]:
        congratulate()


if __name__ == "__main__":
    print("Добро пожаловать в крестики-нолики")
    while game_on:
        draw_field()
        count = shoot(input(),count)
