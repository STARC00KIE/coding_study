alpha = input()
al = list(alpha)
al.append("")
al.append("")
i = 0
cnt = 0

while i<(len(al)-2):
    if al[i] == 'c' or al[i] == 'l' or al[i] == 'n' or al[i] == 's' or al[i] == 'z':
        tmp = al[i]+al[i+1]
        if tmp == 'c=' or tmp == 'c-' or tmp == 'lj' or tmp == 's=' or tmp == 'z=' or tmp == 'nj':
            i += 1
    elif al[i] == 'd':
        tmp = al[i]+al[i+1]
        if tmp == 'd-':
            i += 1
        elif tmp == 'dz':
            tmp += al[i+2]
            if tmp == 'dz=':
                i += 2
    cnt += 1 
    i += 1

print(cnt)