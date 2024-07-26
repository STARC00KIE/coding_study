def solution(arr, queries):
    answer = []
    for query in queries:
        tmp = []
        for i in range(len(arr)):
            if query[0] <= i and i <= query[1] and arr[i] > query[2]:
                tmp.append(arr[i])
            # print(f'tmp: {tmp}')
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)
        # print(f'answer: {answer}')
    return answer