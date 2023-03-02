test_num = int(input())
score = [list(map(int, input().split())) for _ in range(test_num)]
std_num = []

for i in range(test_num):
    std_num.append(score[i].pop(0))

for i in range(test_num):
    cnt = 0
    tmp = sum(score[i])/std_num[i]
    for j in range(len(score[i])):
        if score[i][j] > tmp:
            cnt += 1
    result = (cnt/std_num[i])*100
    print(f"{result:.3f}%")