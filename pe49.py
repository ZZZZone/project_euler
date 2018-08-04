import math


def solve(x):
    a = []
    while x != 0: 
        a.append(str(x % 10))
        x //= 10
    a.sort()
    return int(''.join(a))


n = 100000
is_prime = {i:True for i in range(1, 10*n+1)}
prime = []

for i in range(2, n+1): # 筛素数
    if is_prime[i] == True:
        prime.append(i)
        for j in range(i * i, 10*n + 1, i):
            is_prime[j] = False

les = 2
for i in prime:
    if les <= 0: break
    if i < 1000: continue
    for j in range(1, n):
        if is_prime[i+j] == False or is_prime[i+j*2] == False: continue
        if i+j >= 10000 or i+2*j >= 10000: break
        a = solve(i); b = solve(i+j);c = solve(i+2*j)
        if a == b and a == c:
            print(i, i+j, i +2*j)
            print(str(i)+ str(i+j)+str(i+j*2))
            les -= 1


