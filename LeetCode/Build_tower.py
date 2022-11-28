def tower_builder(n_floors: int) -> list:
    a = "*"
    arr = []
    for i in range(1, n_floors * 2, 2):
        if i % 2 != 0:
            arr.append(f'{a * i:^{n_floors * 2 - 1}}')
    for i in arr:
        print(i)
    return arr


tower_builder(10)
