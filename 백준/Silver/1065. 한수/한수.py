N = int(input())
def han(N):
    cnt = 0
    nums = list(range(1, N+1))
    for number in nums:
        if (number//10) == 0:    # 1의자리
            cnt += 1
        elif (number//100) == 0: # 10의 자리
            cnt += 1
        elif (number//1000) == 0:
            tmp = []
            for n in str(number):
                tmp.append(int(n))
            if (tmp[0]-tmp[1]) == (tmp[1]-tmp[2]):
                cnt += 1
    print(cnt)

han(N)