def solution(arr, query):
    for idx, a in enumerate(query):
        if idx % 2 == 0:
            del(arr[a+1:])
        else:
            del(arr[:a])
    return arr