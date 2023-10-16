field = [[" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "],
         ["X", " ", "X", " ", "X", " ", "X", " ", "X"],
         [" ", "O", " ", "O", " ", "O", " ", "O", " "]]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
my_dict = {j: i for i, j in enumerate(letters)}


def draw_field():
    print("\t\t\t\t\t\t\t\tБерег Ноликов")
    print("\t\t\t\t" + "-" * 41)
    for i, k in enumerate(field):
        if i == 4:
            print("Берег крестиков", end=" |")
            for j in k:
                print(f"\t{j}", end="")
            print(f"\t| {i + 1}", end="")
            print("   Берег крестиков")
        else:
            print("\t\t\t\t|", end="")
            for j in k:
                print(f"\t{j}", end="")
            print("\t|", i + 1)
    print("\t\t\t\t" + "-" * 41)
    print("\t\t\t\t\t", end="")
    print(("\t").join(letters))
    print()
    print("\t\t\t\t\t\t\t\tБерег ноликов")


draw_field()
