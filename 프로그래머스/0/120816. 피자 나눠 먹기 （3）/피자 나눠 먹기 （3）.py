def solution(slice, n):
    pizza = 0
    cnt = 1
    while True:
        pizza += slice
        if (pizza//n) >= 1:
            return cnt
        else:
            cnt += 1