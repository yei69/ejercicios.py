arr = [1, 3, 4, 2, 7, 0]
for i in arr:
    for j in arr:
        if i + j == 10:
            print(f"Los elementos son {i} y {j}")
            break