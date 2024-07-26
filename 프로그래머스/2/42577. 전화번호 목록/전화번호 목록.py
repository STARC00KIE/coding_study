def solution(phone_book):
    phone_book.sort() # 정렬
    
    # 한 번호가 다른 번호의 접두어인 경우 확인
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
