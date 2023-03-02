subj_num = int(input())
subj_score = []
result_lst = []

for i in range(subj_num):
    subj_score.append(list(input()))

for i in range(subj_num):
    result = 0
    tmp = 1
    for j in range(len(subj_score[i])):
        if subj_score[i][j] == 'X':
            tmp = 1
        elif subj_score[i][j] == 'O':
            result += tmp
            tmp += 1
    print(result)