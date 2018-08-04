
million = 1000000
fac = [0] * 105
fac[0] = 1
cnt = 0
for i in range(1, len(fac)): 
    fac[i] = fac[i-1] * i


def Solve(n, m):
    ans = fac[n] // fac[m] // fac[n-m]
    global cnt
    if ans > million: cnt += 1


for i in range(100):
    for j in range(i):
        Solve(i+1, j+1)
print(cnt)

