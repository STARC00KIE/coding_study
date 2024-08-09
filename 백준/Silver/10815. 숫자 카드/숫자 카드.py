n1 = int(input())
l1 = set(map(int, input().split()))
n2 = int(input())
l2 = list(map(int, input().split()))

answer = []
for i in l2:
    if i in l1:
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a,end=" ")