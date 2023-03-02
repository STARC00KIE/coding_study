cnt = int(input())
res = []
for i in range(cnt):
    n1, n2 = map(int, input().split())
    res.append(n1+n2)

for i in range(cnt):
    print(res[i])