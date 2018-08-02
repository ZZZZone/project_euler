
is_prime = {}
n = 1000000
les = 11
Sum = 0

def GetPrime(): # 筛素数
    for i in range(1, n + 1):
        is_prime[i] = True
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i] == True:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False


def check(val):
    s = str(val)
    t = s[:]
    for i in range(0, len(s)):
        if is_prime[int(s)] == False: return False
        s = s[1:]
    for i in range(0, len(t)):
        if is_prime[int(t)] == False: return False
        t = t[:-1]
    return True
        
GetPrime()
for i in range(10, n+1):
    if les <= 0 : break
    if check(i) :
        print(i)
        Sum += i
        les -= 1

print(Sum)

