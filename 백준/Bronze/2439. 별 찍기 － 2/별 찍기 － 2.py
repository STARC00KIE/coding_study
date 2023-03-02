cnt = int(input())
star = '*'
for i in range(cnt):
    print('{}'.format(str(star*(i+1))).rjust(cnt))