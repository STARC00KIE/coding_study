pred = int(input())
cnt = int(input())
total = 0
for i in range(cnt):
    price, num = map(int, input().split())
    total += (price*num)

if pred == total:
    print('Yes')
else:
    print('No')