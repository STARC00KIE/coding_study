def solution(my_string):
    lst = list(my_string)
    answer = ''
    for l in lst:
        if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':
            pass
        else:
            answer+=l
    return answer