def solution(myString, pat):
    answer = ''
    for i in range(0,len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat and len(pat) != 1:
            return myString[0:i+len(pat)]
        elif myString[i:i+len(pat)] == pat and len(pat) == 1:
            answer = myString[0:i+len(pat)]
            
    return answer