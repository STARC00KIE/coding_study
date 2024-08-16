def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    if len(pat) > len(myString):
        return 0
    for i in range(0, len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            return 1
    
    return 0
        