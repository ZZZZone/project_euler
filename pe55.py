cnt = 0
n = 10000

def Solve(num):
    s1 = str(num)
    s2 = s1[::-1]
    for i in range(50):
        num += int(s2)
        s1 = str(num)
        s2 = s1[::-1]
        if s1 == s2:
            return True
    return False



for i in range(n):
    if Solve(i) == False:
        cnt += 1

print(cnt)


