def solution(arr):
    num = 0
    
    
    while True:
        cnt = 0

        for i, a in enumerate(arr):
            if a > 50 and a%2 == 0:
                arr[i] = a//2
            elif a < 50 and a%2 == 1:
                arr[i] = a*2+1
            else:
                cnt += 1
                
        if len(arr) == cnt:
            return num
        num += 1
            