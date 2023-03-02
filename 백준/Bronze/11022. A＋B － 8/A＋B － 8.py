import sys
cnt = int(input())
res = []
n1l = []
n2l = []
for i in range(cnt):
    n1, n2 = map(int, sys.stdin.readline().split())
    n1l.append(n1)
    n2l.append(n2)
    res.append(n1+n2)

for i in range(cnt):
    print('Case #{}: {} + {} = {}'.format(str(i+1), str(n1l[i]), str(n2l[i]), str(res[i])))
