
million = 1000001
is_prime = {i:True for i in range(1, million)}
prime = []
res = [0] * million

is_prime[1] = False
for i in range(2, million): #筛素数
    if is_prime[i] == True:
        prime.append(i)
        for j in range(i * i, million, i):
            is_prime[j] = False

Max = 0; ans = 0

for i in range(0, len(prime)):
    now = 0
    cnt = 0
    for j in range(i, len(prime)):
        now += prime[j]
        cnt += 1
        if now >= million: break; 
        if is_prime[now] == True:
            if cnt > Max:
                Max = cnt
                ans = now

print(ans)
