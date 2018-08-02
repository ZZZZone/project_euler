import math
n = 1000000

def solve(x):
    res = 0
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0: res += 1
        while(x % i == 0) :
            x //= i
    if x != 1: res += 1
    #print(x, res)
    return res

for i in range(1, n):
    if solve(i) == 4 and solve(i+1) == 4 and solve(i+2) == 4 and solve(i+3) == 4:
        print(i)
        break
