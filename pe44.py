n = 5000
vis = {i:False for i in range(0,100000000)}

for i in range(1, 10000000):
    vis[i * (3 * i - 1) // 2] = True

ans = 1 << 30
for i in range(1, n):
    x = i * (3 * i - 1) // 2
    for j in range(i, n):
        y = j * (3 * j - 1) // 2
        if vis[x+y] == True and vis[y-x] == True: 
            print(y-x)
            ans = min(ans, y-x)
print(ans)
