from coloroma import Fore

nums_str = (int(j) for i in range(1, 20) for j in str(i) if i != 10)
start_field = [[next(nums_str) for j in range(9)] for i in range(3)]
temp_field = start_field.copy()
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
my_dict = {j: i for i, j in enumerate(letters)}


def draw_field():
    print("-" * 35)
    for i in range(len(start_field)):
        for j in range(len(start_field[i])):
            print(f" {start_field[i][j]} ", end="|") if temp_field[i][j] != 0 else print(Fore.Red, f" {start_field[i][j]} ", end="|")
        print(f"\t {i + 1}")
        print("-" * 35)
    print(" " + "   ".join(letters))


def check_field():
    for i in range(len(temp_field) - 1):
        for j in range(len(start_field[i] - 1)):
            if (temp_field[i][j] == temp_field[i + 1][j] or temp_field[i][j] + temp_field[i + 1][j] == 10 or \
                temp_field[i][j] == temp_field[i][j + 1] or temp_field[i][j] + temp_field[i][j + 1] == 10) and \
                    temp_field[i][j] != 0:
                return True
    for i in range(len(temp_field[-1]) - 1):
        if temp_field[-1][i] == temp_field[-1][i + 1] or temp_field[-1][i] + temp_field[-1][i + 1] == 10:
            return True
    return False


def check_step(letter_num1, letter_num2):
    letter1 = letter_num1[0]
    num1 = int(letter_num1[1])
    letter2 = letter_num2[0]
    num2 = int(letter_num2[1])
    if temp_field[num1][my_dict[letter1]] == temp_field[num2][my_dict[letter2]] \
            or temp_field[num1][my_dict[letter1]] + temp_field[num2][my_dict[letter2]] == 10:
        temp_field[num1][my_dict[letter1]] = 0
        temp_field[num2][my_dict[letter2]] = 0

# draw_field()
