def solution(sides):
    long = max(sides)
    short = sum(sides) - long
    
    if long < short:
        return 1
    else:
        return 2
