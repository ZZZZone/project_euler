
cnt = 0
ans = 0

def Solve(x):
    res = 0
    for i in range(1, x):
        for j in range(i, x):
            k = x - i - j
            if k < j: continue
            a = min(i, j, k)
            c = max(i, j, k)
            b = x - a - c
            if a > 0 and a * a + b * b == c * c:
                res += 1
    return res


for p in range(1, 1001):
    tmp = Solve(p)
    if tmp > cnt:
        ans = p
        cnt = tmp

print(ans)
print(cnt)

