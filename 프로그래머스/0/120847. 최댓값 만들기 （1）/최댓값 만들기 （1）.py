def solution(numbers):
    n1 = numbers.pop(numbers.index(max(numbers)))
    n2 = numbers.pop(numbers.index(max(numbers)))
    return n1*n2