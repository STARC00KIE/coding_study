def solution(my_string):
    my_string = list(my_string.split(" "))
    operator = ''
    answer = int(my_string.pop(0))
    
    for m in my_string:

        if m == '+':
            operator = 'plus'
        elif m == '-':
            operator = 'minus'
            
        elif m.isdigit():
            if operator == 'plus':
                answer += int(m)
            else:
                answer -= int(m)
    
    return answer
