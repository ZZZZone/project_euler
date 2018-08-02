import math

def Solve(a, b):
    i = 0
    while(True):
        x = i * i + a * i + b
        if x <= 1:
            return i
        if is_prime[x] == False:
            return i
        i += 1

'''
筛素数
'''
is_prime = {}
prime = []
n = 10000000
for i in range(2, n+1):
    is_prime[i] = True
for i in range(2, n+1):
    if(is_prime[i] == True):
        prime.append(i)
        for j in range(i * i, n+1, i):
            is_prime[j] = False


res = 0; now = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        tmp = Solve(a, b)
        if tmp > now:
            now = tmp; res = a * b
print(res)
print(now)

            

