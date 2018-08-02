import math
n = 10
ans = 0

def check(Sum):
    for i in range(2, math.ceil(math.sqrt(Sum))):
        if Sum % i == 0 : return False
    return True

def Dfs(dis, Sum, tot):
    if dis == tot and check(Sum):
        global ans
        ans = max(ans, Sum)
    for i in range(1, tot+1):
        if vis[i] == False:
            vis[i] = True
            Dfs(dis+1, Sum * 10 + i, tot)
            vis[i] = False


vis = {}

for i in range(1, 100):
    vis[i] = False

for i in range(1, n):
    ans = 0
    Dfs(0, 0, i)
    print(ans)
