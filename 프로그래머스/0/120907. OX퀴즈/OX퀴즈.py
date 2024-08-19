def solution(quiz):
    answer = []
    for q in quiz:
        tmp = q.split(" ")
        result = 0
        if tmp[1] == "+":
            result = int(tmp[0]) + int(tmp[2])
            if result == int(tmp[4]):
                answer.append('O')
            else:
                answer.append('X')
        
        if tmp[1] == "-":
            result = int(tmp[0]) - int(tmp[2])
            if result == int(tmp[4]):
                answer.append('O')
            else:
                answer.append('X')
                
    return answer