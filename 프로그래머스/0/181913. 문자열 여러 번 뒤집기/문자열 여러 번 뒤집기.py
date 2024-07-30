def solution(my_string, queries):
    my_list = list(my_string)

    for q in queries:
        tmp = list(reversed(my_list[q[0]:q[1]+1]))
        my_list[q[0]:q[1]+1] = tmp

    return "".join(my_list)