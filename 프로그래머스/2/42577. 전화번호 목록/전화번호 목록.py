
"""
# 실패한 케이스

def solution(phone_book):
    N = phone_book.pop(0)  # 구조대 번호
    
    for num in phone_book:
        if num.startswith(N):
            return False
    return True
"""

def solution(phone_book):
    phone_book.sort() # 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
