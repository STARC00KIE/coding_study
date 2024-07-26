def solution(arr, queries):
    tmp_1 = 0
    tmp_2 = 0
    for i in range(len(queries)):
        tmp_1 = arr[queries[i][0]]
        tmp_2 = arr[queries[i][1]]
        
        arr[queries[i][1]] = tmp_1
        arr[queries[i][0]] = tmp_2

    return arr