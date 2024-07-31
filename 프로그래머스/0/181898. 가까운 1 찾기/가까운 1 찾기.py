def solution(arr, idx):
    answer = 0
    for i, a in enumerate(arr):
        if a==1 and i>=idx:
            return i

    return -1