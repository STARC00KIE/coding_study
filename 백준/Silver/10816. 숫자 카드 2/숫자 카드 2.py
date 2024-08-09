from collections import Counter

# 입력을 받습니다.
n1 = int(input())
l1 = list(map(int, input().split()))
n2 = int(input())
l2 = list(map(int, input().split()))

# l1의 요소 개수를 세는 Counter 객체를 만듭니다.
counter = Counter(l1)

# l2의 각 요소에 대해 l1에서의 개수를 출력합니다.
for i in l2:
    print(counter.get(i, 0), end=" ")