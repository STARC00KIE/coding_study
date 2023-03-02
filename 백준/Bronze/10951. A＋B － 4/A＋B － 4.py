n1l = []
n2l = []
res = 0

while(1):
    try:
        n1, n2 = map(int, input().split())
        n1l.append(n1)
        n2l.append(n2)
    except:
        break

for i in range(len(n1l)):
    res = n1l[i]+n2l[i]
    print(res)