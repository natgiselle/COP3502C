def min_terms(n):
    sum = 0
    a = 0
    x = 0
    count = 0
    # stops when sum > n
    while sum <= n:
        a += 1
        x += 2
        sum += (a**a)/x
        count += 1
    print(count)

min_terms(100)
        # 1^1/2 + 2^2/4
