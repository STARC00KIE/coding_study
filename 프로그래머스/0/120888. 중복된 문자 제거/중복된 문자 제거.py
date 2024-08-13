def solution(my_string):
    lst = []
    for s in my_string:
        if not s in lst:
            lst.append(s)

    return "".join(lst)