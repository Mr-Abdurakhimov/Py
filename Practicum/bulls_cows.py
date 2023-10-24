from random import randint


def make_a_number():
    return randint(1000, 9999)


def check_for_bull(num_riddled, num_from_player):
    count = 0
    start = 1
    for i in range(4):
        if (num_riddled // start % 10) == (num_from_player // start % 10):
            count += 1
        start *= 10
    return count


def check_for_cow(num_riddled, num_from_player):
    count = 0
    start = 1
    for i in range(4):
        if (str(num_from_player // start % 10) in str(num_riddled)) and not (
                (num_riddled // start % 10) == (num_from_player // start % 10)):
            count += 1
        start *= 10
    return count


game_on = True
num = make_a_number()
while game_on:
    print("Введите число: ", end="")
    trial = int(input())
    if trial == num:
        print("Поздравляем, вы угадали число !")
        game_on = False
        break
    bulls = check_for_bull(num, trial)
    cows = check_for_cow(num, trial)
    print(f"Коров: {cows}\nБыков: {bulls}")
