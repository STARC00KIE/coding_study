def solution(n):
    pizza = 0
    cnt = 1
    while True:
        pizza += 7
        if (pizza//n) >= 1:
            return cnt
        else:
            cnt += 1