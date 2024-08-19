def solution(myString):
    my = myString.split("x")
    answer = []
    for m in my:
        answer.append(len(m))
        
    return answer