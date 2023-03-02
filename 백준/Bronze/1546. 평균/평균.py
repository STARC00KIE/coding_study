subj_num = int(input())
subj_score = list(map(int, input().split()))
new_score = []

def cal1(a):
    return (a/max(subj_score))*100

new_score = list(map(cal1, subj_score))
result = sum(new_score)/subj_num

print(f"{result}")