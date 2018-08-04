ans = 0
for a in range(100):
    for b in range(100):
        num = a ** b
        tmp = 0
        while num != 0:
            tmp += num % 10
            num //= 10
        ans = max(ans, tmp)
print(ans)
