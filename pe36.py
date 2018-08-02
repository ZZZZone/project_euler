import operator
million = 1000000
ans = 0

'''
python3 中取消的cmp函数
所以无法用cmp直接比较两个列表
需要用operator
'''
def check10(val):
    a = [str(val)[i] for i in range(0, len(str(val)))]
    b = a[:]
    b.reverse()
    return operator.eq(a, b)

def check2(val):
    a = []
    b = []
    while val != 0:
        a.append(val % 2)
        val //= 2
    b = a[:]
    b.reverse()
    return operator.eq(a, b)

Sum = 0
for i in range(1, million+1):
    if check2(i) and check10(i):
        ans += 1
        Sum += i
        print(i)
print(ans)
print(Sum)


