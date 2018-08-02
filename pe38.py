Max = 0
now = 0


def is_pandigital(val):
    s = str(val)
    for i in range(2, 10):
        s += (str(val*i))
        if len(s) >= 9: break
    if len(s) != 9: return 0
    t = [s[i] for i in range(0, len(s))]
    t.sort()
    if int(''.join(t)) == 123456789 : return int(s)
    return 0

for i in range(1, 1000000):
    tmp = is_pandigital(i)
    if tmp > Max:
        Max = tmp
        now = i

print(Max)
print(now)
