div_lst = []
# remove_set = {0}

for i in range(10):
    div_lst.append(int(input())%42)

div_lst = list(set(div_lst))
# div_lst = [j for j in div_lst if j not in remove_set] # remove remove_set in div_lst

print(f"{len(div_lst)}")