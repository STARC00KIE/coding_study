def solution(num, k):
    numlist = list(str(num))
    print(numlist)
    for i, n in enumerate(numlist):
        if int(n) == k:
            return i+1
    return -1