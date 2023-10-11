field_syms = [[" " for j in range(10)] for i in range(10)]


def draw_field():
    print("-" * 60)
    for i in range(10):
        for j in range(10):
            print(f"  {field_syms[i][j]}  |", end="")
        print()
        print("-" * 60)


def make_a_step(line, row):
    field_syms[line][row] = "*"


def check_vertical(line, row):
    minimal_line = line - 1 if line - 1 >= 0 else line
    maximal_line = line + 1 if line + 1 < 10 else line
    count = 0
    temp = 0
    for i in range(minimal_line, maximal_line + 1):
        if field_syms[i][row] == "*" and i != line:
            count += 1
            temp = i
    if count == 2:
        return False
    elif count == 1 and temp < line:
        if temp - 1 >= 0:
            if field_syms[temp - 1][row] == "*":
                return False
    elif count == 1 and temp > line:
        if temp + 1 < 10:
            if field_syms[temp + 1][row] == "*":
                return False
    return True


def check_horizontal(line, row):
    minimal_row = row - 1 if row - 1 > 0 else row
    maximal_row = row + 1 if row + 1 < 10 else row
    count = 0
    temp = 0
    for i in range(minimal_row, maximal_row + 1):
        if field_syms[line][i] == "*" and i != row:
            count += 1
            temp = i
    if count == 2:
        return False
    elif count == 1 and temp < row:
        if temp - 1 >= 0:
            if field_syms[line][temp - 1] == "*":
                return False
    elif count == 1 and temp > row:
        if temp + 1 < 10:
            if field_syms[line][temp + 1] == "*":
                return False
    return True


def check_diagonal(line, row):
    count_side_diagonal = 0
    count_main_diagonal = 0
    for i in range(1, 3):
        if line - i >= 0 and row - i >= 0:
            if field_syms[line - i][row - i] == "*":
                count_side_diagonal += 1
        if line + i < 10 and row + i < 10:
            if field_syms[line + i][row + i] == "*":
                count_side_diagonal += 1
    for i in range(1,3):
        if line - i >= 0 and row + i < 10:
            if field_syms[line - i][row + i] == "*":
                count_main_diagonal += 1
        if line + i < 10 and row - i >= 0:
            if field_syms[line + i][row - i] == "*":
                count_main_diagonal += 1

    if count_side_diagonal >= 2 or count_main_diagonal >=2:
        return False
    return True


def check_for_ending(line, row):
    res_vertical = check_vertical(line, row)
    res_horizontal = check_horizontal(line, row)
    res_diagonal = check_diagonal(line, row)
    if res_horizontal and res_vertical and res_diagonal:
        return True
    else:
        draw_field()
        print("Игра окончена")
        return False


if __name__ == "__main__":
    game_on = True
    while game_on:
        draw_field()
        coors = [int(i) - 1 for i in input().split()]
        make_a_step(coors[0], coors[1])
        game_on = check_for_ending(coors[0], coors[1])
