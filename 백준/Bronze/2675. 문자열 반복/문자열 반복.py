num = int(input())
rep = []
char = []

for i in range(num):
    tmp1, tmp2 = map(str, input().split())
    rep.append(int(tmp1))
    char.append(tmp2)

for i in range(num):
    res = ""
    for ch in list(char[i]):
        res += (ch*rep[i])
    print(res)
