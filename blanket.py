places = [[" " for i in range(5)] for j in range(4)]
signs = {1: "@", 2: "*"}
score_dict = {1: 0, 2: 0}
player = 1


def drawField():
    for i in range(4):
        print("-" * 15)
        for j in range(5):
            print(f"{places[i][j]} |", end="")
        print()
    print("-" * 15, f"\tСчет штрафов 1 игрока : {score_dict[1]}\t Счет штрафов 2 игрока : {score_dict[2]}")


def make_a_step(player, line, row):
    global score
    places[line][row] = signs[player]
    check(player, line, row)


def check(player, line, row):
    global score
    minimal_line = line
    maximal_line = line
    maximal_row = row
    minimal_row = row
    if line > 0:
        minimal_line = line - 1
    if line < 3:
        maximal_line = line + 1
    if row > 0:
        minimal_row = row - 1
    if row < 4:
        maximal_row = row + 1
    for i in range(minimal_line, maximal_line + 1):
        for j in range(minimal_row, maximal_row + 1):
            if (places[i][j] != "") and (places[i][j] == places[line][row]) and (i != line or j != row):
                score_dict[player] += 1


def game_not_over():
    for i in places:
        if " " in i:
            return True
    return False



def congratulate():
    winner = 1 if score_dict[1] < score_dict[2] else 2
    print(f"Игрок {winner} победил, у него меньше штрафов")

if __name__ == "__main__":
    while game_not_over():
        drawField()
        a = [(int(i) - 1) for i in input().split()]
        make_a_step(player, a[0], a[1])
        if player == 1:
            player = 2
        else:
            player = 1
    congratulate()
