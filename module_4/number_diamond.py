# Top half (pyramid)
h = int(input("type: "))
for i in range(1, h+1):
    spaces = " " * (h - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)

# Bottom half (inverted)
for i in range(h-1, 0, -1):
    spaces = " " * (h - i)
    stars = "*" * (2*i - 1)
    print(spaces + stars)