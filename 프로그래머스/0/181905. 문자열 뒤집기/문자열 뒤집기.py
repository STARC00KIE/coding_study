def solution(my_string, s, e):
    if len(my_string) == e:
        reverse_s = "".join(reversed(my_string[s:e+1]))
        return my_string[:s] + reverse_s + my_string[e+1:]
    else:
        reverse_s = "".join(reversed(my_string[s:e+1]))
        return my_string[:s] + reverse_s + my_string[e+1:]