def solution(n):
    cnt = 1
    num = 1
    while True:
        num = num*cnt
        if num == n:
            return cnt
        elif num > n:
            return cnt-1
        cnt += 1