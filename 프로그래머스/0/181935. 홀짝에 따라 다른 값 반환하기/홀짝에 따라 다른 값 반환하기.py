def solution(n):
    
    if n%2 != 0: # 홀수일 떼
        cnt = 1
        num = 0
        while n >= cnt:
            num += cnt
            cnt += 2
    else: # 짝수일 때
        cnt = 2
        num = 0
        while n >= cnt:
            num += (cnt**2)
            cnt +=2
    return num