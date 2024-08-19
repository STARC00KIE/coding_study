def solution(myString, pat):
    newstr= ""
    for i, my in enumerate(myString):
        if my == 'A':
            newstr += 'B'
        else:
            newstr += 'A'
    
    if pat in newstr:
        return 1
    return 0