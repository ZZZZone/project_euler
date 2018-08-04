n = 1000000

def Solve(val):
    tmp = val
    lists = []
    list2 = []
    while tmp != 0:
        lists.append(str(tmp % 10))
        tmp //= 10
    for i in range(2, 7):
        now = val * i
        list2.clear()
        while now != 0:
            list2.append(str(now % 10))
            now //= 10
        if ''.join(sorted(lists)) != ''.join(sorted(list2)): return False
        list2.reverse()
        print(list2)
    print(val)
    return True

for i in range(1, n):
    if Solve(i):
        break

