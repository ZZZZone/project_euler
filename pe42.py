File = open("p042_words.txt")
str = File.read()
a = str.split(',')
cnt = 0

def check(s):
    res = 0
    #print(s)
    for i in s[1:-1]:
        res += ord(i) - ord('A') + 1
    for i in range(10000):
        if i * (i + 1) // 2 == res: return True
    return False


for i in a[:]:
    if check(i):
        cnt += 1
print(cnt)


File.close()
