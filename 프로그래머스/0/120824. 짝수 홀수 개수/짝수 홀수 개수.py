def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        # 짝수
        if i%2 == 0:
            even += 1
        else:
            odd +=1
        # 홀수
    return [even, odd]