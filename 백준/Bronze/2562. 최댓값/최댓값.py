num_lst = []

for i in range(9):
    num_lst.append(int(input()))

max_lst = max(num_lst)
max_cnt = num_lst.index(max(num_lst)) + 1

print(f"{max_lst}\n{max_cnt}")