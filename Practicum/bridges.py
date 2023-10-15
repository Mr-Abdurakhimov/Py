field = [[" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "]]


def draw_field():
    print("\t\t\t\t\t\t\t\tБерег Ноликов")
    print("\t\t\t\t" + "-" * 41)
    for i, k in enumerate(field):
        if i == 4:
            print("Берег крестиков", end=" |")
            for j in k:
                print(f"\t{j}", end="")
            print("\t|", end="")
            print("  Берег крестиков")
        else:
            print("\t\t\t\t|", end="")
            for j in k:
                print(f"\t{j}", end="")
            print("\t|")
    print("\t\t\t\t" + "-" * 41)
    print("\t\t\t\t\t\t\t\tБерег ноликов")


draw_field()
