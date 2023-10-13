nums_str = (int(j) for i in range(1,20) for j in str(i) if i != 10)
start_field = [[next(nums_str) for j in range(9)]for i in range(3)]

def draw_field():
    print("-" * 35)
    for i in range(3):
        for j in range(9):
            print(f" {start_field[i][j]} ", end="|")
        print()
        print("-" * 35)

draw_field()