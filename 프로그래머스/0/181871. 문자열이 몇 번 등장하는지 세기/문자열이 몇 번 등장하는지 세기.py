def solution(myString, pat):
    cnt = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:len(pat)+i] == pat:
            cnt += 1
    
    return cnt