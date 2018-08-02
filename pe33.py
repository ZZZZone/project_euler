

def gcd(a, b):
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)

numerator = 1
denominator = 1


for a in range(10, 100):
    for b in range(a+1, 100):
        x1 = a // 10; x2 = a % 10
        y1 = b // 10; y2 = b % 10
        tx = a // gcd(a, b)
        ty = b // gcd(a, b)
        if x2 == y1  and tx * y2 == ty * x1: numerator *= a; denominator *= b
        Gcd = gcd(numerator, denominator)
        numerator //= Gcd
        denominator //= Gcd
print(str(numerator) + '/' + str(denominator))




