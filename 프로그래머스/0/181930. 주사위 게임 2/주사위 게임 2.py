def solution(a, b, c):
    if (a != b) and (b != c) and (c != a):
        print(0)
        return a+b+c
    elif a==b and b==c and c==a:
        print(1)
        return (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    else:
        print(2)
        return (a+b+c) * (a**2+b**2+c**2)