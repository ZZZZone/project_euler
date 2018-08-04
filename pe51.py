
million = 1000000
is_prime = {i:True for i in range(1, million)}
primes = []
res = [0] * million


def Solve(pr):
    array = []
    tmp = pr
    while tmp != 0:
        array.append(str(tmp % 10))
        tmp //= 10
    array.reverse()
    for i in range(0, (1 << (len(array)))):
        que = []
        que.clear()
        lists = array.copy()
        tot = 0
        for j in range(10):
            for k in range(len(array)):
                if ((1 << k) & i) != 0:
                    lists[k] = str(j)
            if lists[0] == '0': continue
            now = int(''.join(lists))
            if is_prime[now] == True and que.count(now) == 0:
                tot += 1
                que.append(now)
        if tot == 8:
            que.sort()
            print(que)
            print(que[0])
            return True
    return False



is_prime[1] = False
for i in range(2, million): #筛素数
    if is_prime[i] == True:
        primes.append(i)
        for j in range(i * i, million, i):
            is_prime[j] = False


ans = 0; Max = 0
for i in primes:
    if Solve(i) == True:
        #print(i)
        break
