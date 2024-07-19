def solution(want, number, discount):
    # want, number 딕셔너리 만들기
    want_dic = {}
    answer = 0
    
    for w,n in zip(want, number):
        want_dic[w] = n
        
    # dict 10일씩 잘라서 딕셔너리 만들기
    for i in range(len(discount)-9):
        disc10_dic = {}
        # 딕셔너리 값 넣기
        for j in range(i, i+10):
            if discount[j] in disc10_dic:
                disc10_dic[discount[j]] += 1
                
            else:
                disc10_dic[discount[j]] = 1
                
        # want dict랑 비교
        if disc10_dic == want_dic:
            answer += 1
            
    return answer