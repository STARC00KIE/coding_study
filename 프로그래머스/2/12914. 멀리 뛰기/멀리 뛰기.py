def fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result
import math
def solution(n):
    cnt1 = n%2
    cnt2 = n//2
    n = n//2
    answer = 0
    
    while n >= 0:
        answer += math.factorial(cnt1+cnt2)//(math.factorial(cnt2) * math.factorial(cnt1))
        n -= 1
        cnt1 += 2
        cnt2 -= 1
    return answer % 1234567