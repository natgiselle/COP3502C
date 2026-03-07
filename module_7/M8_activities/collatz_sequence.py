def collatz_sequence(n):
    if n == 1:
        print(n)
        return
    else:
        print(n, end = " ")
        if n % 2 == 0:
            return collatz_sequence(n//2)
        else:
            return collatz_sequence(3 * n + 1)

for n in range(1,10):
    collatz_sequence(n)