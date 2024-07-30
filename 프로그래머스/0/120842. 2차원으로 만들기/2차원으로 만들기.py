def solution(num_list, n):
    # n이 2일때 01 23 45 67 로 나뉨
    # n이 3일때 012 345 678 91011
    tmp = []
    answer = []
    
    cnt = 1
    for num in num_list:
        tmp.append(num)
        if cnt%n == 0:
            answer.append(tmp)
            tmp = []
        cnt +=1
    return answer