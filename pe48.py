Mod = 10000000000

def fast_pow(x, y):
    res = 1
    while y != 0:
        if y & 1: res = res * x % Mod
        y >>= 1
        x = x * x % Mod
    return res

ans = 0
for i in range(1, 1001):
    ans = ans + fast_pow(i, i)
    ans %= Mod

print(ans)
