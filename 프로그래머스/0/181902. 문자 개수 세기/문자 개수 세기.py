def solution(my_string):
    lower = [0 for x in range(26)]
    upper = [0 for x in range(26)]
    
    for s in my_string:
        if 97 <= ord(s) and ord(s) <= 122:
            lower[ord(s) - 97] += 1
        else:
            upper[ord(s) - 65] += 1
    return upper + lower