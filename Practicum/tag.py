from random import shuffle
import keyboard

my_gen = (int(i) for i in range(0, 16))
nums = [[next(my_gen) for j in range(4)] for i in range(4)]
win_set = nums.copy()


def find_zero():
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] == 0:
                lst = [i, j]
                return lst


def put_zero_first(i, j):
    nums[0][0], nums[i][j] = nums[i][j], nums[0][0]


def draw_field():
    for i in nums:
        print("-" * 20)
        for j in i:
            if len(str(j)) < 2:
                print(f" {j} ", end=" |")
            else:
                print(f" {j} ", end="|")
        print()
    print("-" * 20)


def mix():
    for i in nums:
        shuffle(i)
    shuffle(nums)


def go_up(coors):
    if coors[0] != 0:
        nums[coors[0] - 1][coors[1]], nums[coors[0]][coors[1]] = nums[coors[0]][coors[1]], nums[coors[0] - 1][coors[1]]
    else:
        print("Некуда идти")


def go_down(coors):
    if coors[0] != len(nums):
        nums[coors[0] + 1][coors[1]], nums[coors[0]][coors[1]] = nums[coors[0]][coors[1]], nums[coors[0] + 1][coors[1]]
    else:
        print("Некуда идти")


def go_left(coors):
    if coors[1] != 0:
        nums[coors[0]][coors[1] - 1], nums[coors[0]][coors[1]] = nums[coors[0]][coors[1]], nums[coors[0]][coors[1] - 1]
    else:
        print("Некуда идти")


def go_right(coors):
    if coors[1] != len(nums):
        nums[coors[0]][coors[1] + 1], nums[coors[0]][coors[1]] = nums[coors[0]][coors[1]], nums[coors[0]][coors[1] + 1]
    else:
        print("Некуда идти")


def game_continue():
    for i in range(4):
        if win_set[i] != nums[i]:
            return True
    return False


if __name__ == "__main__":
    mix()
    i, j = find_zero()
    put_zero_first(i, j)
    print("Для того, чтобы двигать нолик используйте стрелочки на клавиатуре.")
    draw_field()
    while game_continue():
        coors = find_zero()
        if keyboard.read_key() == "down":
            go_down(coors)
        elif keyboard.read_key() == "up":
            go_up(coors)
        elif keyboard.read_key() == "right":
            go_right(coors)
        elif keyboard.read_key() == "left":
            go_left(coors)
        else:
            continue
        draw_field()
    print()
    print("Вы выиграли !")