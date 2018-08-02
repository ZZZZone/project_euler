i = 1; j = 1; k = 1
a = 1; b = 1; c = 1

cnt = 2
while cnt > 0:
    i += 1
    a = i * (i + 1) // 2
    while b < a:
        j += 1
        b = j * (3 * j - 1) // 2
    while c < a:
        k += 1
        c = k * (2 * k - 1)
    if a == b and a == c:
        print(a, b, c)
        cnt -= 1

