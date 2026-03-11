print("==== iterating over a nested list ====")
nest = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]


for row in nest:
    print(f"{row}")


# list reduction
print("list reduction")
single_list = []
for row in nest:
    # for eveery row you want every element
    for num in row:
        # row is gonna do row 1,2,3
        single_list.append(num)

print(single_list)
