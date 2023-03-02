n1l = []
n2l = []
res = 0

while(1):
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0:
        break
    else:
        n1l.append(n1)
        n2l.append(n2)

for i in range(len(n1l)):
    res = n1l[i]+n2l[i]
    print(res)