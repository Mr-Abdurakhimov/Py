from random import randint

nums = [1, 2, 3, 4, 5, 6, 7, 8]
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
my_dict = {j: nums[i] for i, j in enumerate(letters)}
hasWon = False


def place_buttons():
    buttons = [[randint(0, 2) for j in range(8)] for i in range(8)]
    return buttons


def make_a_step(step, buttons):
    if step.isdigit():
        buttons[int(step) - 1] = [0] * 8
        return buttons
    elif step in my_dict.keys():
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                buttons[i][my_dict[step] - 1] = 0
        return buttons


def check_for_win(buttons):
    global hasWon
    hasWon = True
    for i in buttons:
        if 1 in i:
            hasWon = False
    return hasWon


def drawField(buttons):
    for i in range(8):
        print("-" * 32)
        for j in range(8):
            if buttons[i][j] == 1:
                print(f" * |", end="")
            else:
                print("   |", end="")
        print(f" {nums[i]}")
    print("-" * 32)
    print(*[f" {i} " for i in letters])

if __name__ == "__main__":
    bt = place_buttons()
    count = 1
    # print(my_dict)
    while not hasWon:
        drawField(bt)
        print(f'Игрок №{count}, ваш ход: ')
        step = input()
        bt = make_a_step(step, bt)
        if check_for_win(bt):
            continue
        if count == 1:
            count = 2
        else:
            count = 1
    print(f'Игрок №{count} победил !!!')
