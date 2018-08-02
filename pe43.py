
Sum = 0

vis = {}

a = [0, 2, 3, 5, 7, 11, 13, 17]

def Solve(val, now):
    if now == 8:
        print(val)
        global Sum 
        Sum += val
        return
    for i in range(0, 10):
        if vis[i] == True: continue
        tmp = val % 100 * 10 + i
        vis[i] = True
        if tmp % a[now] == 0:
            Solve(val * 10 + i, now+1)
        vis[i] = False
    

for i in range(0, 10): vis[i] = False
for i in range(100, 1000):
    tmp = i
    ok = True
    while tmp != 0:
        if vis[tmp % 10] == True: 
            ok = False
        vis[tmp % 10] = True
        tmp //= 10
    if ok:
        Solve(i, 1)
    tmp = i
    while tmp != 0:
        vis[tmp % 10] = False
        tmp //= 10

print("sum =", Sum)
