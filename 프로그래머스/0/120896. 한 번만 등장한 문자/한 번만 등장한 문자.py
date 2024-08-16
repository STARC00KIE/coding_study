def solution(s):
    scnt = set(s)
    
    for sc in scnt:
        if s.count(sc) != 1:
            s = s.replace(sc, '', s.count(sc))
            
    return "".join(sorted(s))