import sys
cnt = int(input())
res = []
for i in range(cnt):
    n1, n2 = map(int, sys.stdin.readline().split())
    res.append(n1+n2)

for i in range(cnt):
    print('Case #{}: {}'.format(str(i+1), str(res[i])))
