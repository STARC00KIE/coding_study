def solution(myString):
    my = myString.split("x")
    my.sort()
    for _ in my:
        if my[0] == "":
            my.pop(0)
        else:
            return my
