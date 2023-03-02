lstnum = int(input())
lst = list(map(int, input().split()))
max = -1000000
min = 1000000

for i in range(lstnum):
    if max < lst[i]:
        max = lst[i]
    if min > lst[i]:
        min = lst[i]
print(f"{min} {max}")
