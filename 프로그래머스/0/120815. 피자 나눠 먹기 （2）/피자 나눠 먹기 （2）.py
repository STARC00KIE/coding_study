def solution(n):
    pizza = 0
    cnt = 1
    while True:
        pizza += 6
        if pizza % n == 0:
            return cnt
        else:
            cnt +=1