import itertools

million = 10000000
res = 0

is_prime = {}


def Check(x):
    a = str(x)
    for i in range(0, len(str(x))): # 循环len次
        if is_prime[int(a)] == False:
            return False
        a = a[1:] + a[:1] #使用切片每次将第一个放到最后
    return True

def GetPrime(): # 筛素数
    for i in range(1, million + 1):
        is_prime[i] = True
    for i in range(2, million + 1):
        if is_prime[i] == True:
            for j in range(i * i, million + 1, i):
                is_prime[j] = False


GetPrime()
for i in range(2, million):
    if Check(i):
        print(i)
        res += 1
print(res)

