def solution(num_list):
    answer = [0, 0]
    for i, n in enumerate(num_list):
        if (i+1) % 2 == 1: # 홀수일 때:
            answer[0] += n
        else:
            answer[1] += n
    return max(answer)