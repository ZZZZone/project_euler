import math
n = 1000000
is_prime = {i:True for i in range(1, n)}
vis = {i:False for i in range(1, n)}
prime = []


def is_comp(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0: return True
    return False

for i in range(2, n):
    if is_prime[i] == True:
        prime.append(i)
        for j in range(i * i, n, i):
            is_prime[j] = False

ans = 1 << 30
for i in prime:
    for j in range(1, 100):
        num = i  + (2 * j * j)
        vis[num] = True

for i in range(2, n):
    if is_comp(i) and (i & 1) and vis[i] == False:
        print(i)
        break
