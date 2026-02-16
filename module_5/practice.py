h = int(input("insert height: "))

for i in range(1, h + 1):
    for j in range(1, h + 1):
        if max(i,j) % 2 == 0:
            print("--", end = "")
        else:
            print("##", end = "")
    print()
