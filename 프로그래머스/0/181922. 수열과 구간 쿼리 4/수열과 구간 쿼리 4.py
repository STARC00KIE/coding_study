def solution(arr, queries):
    answer = arr
    for q in range(len(queries)):
        for i in range(len(arr)):
            if queries[q][0] <= i and i <= queries[q][1] and i%queries[q][2] == 0:
                answer[i] += 1
    return arr