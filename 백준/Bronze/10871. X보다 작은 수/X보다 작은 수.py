import sys
cnt, x = map(int, input().split())
num = [int(x) for x in input().split()]
res = []

for i in range(cnt):
    if num[i] < x:
        res.append(num[i])

for i in range(len(res)):
    print('{}'.format(res[i]), end=' ')