def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        row = i//n
        col = i%n
        
        answer.append(max(row, col)+1)
    
    return answer
    

""" 시간복잡도 초과 코드
def solution(n, left, right):
    
    # 1. 2차원 배열 만들기(빈 배열)
    arr = [[0 for i in range(n)] for i in range(n)]
    
    # 빈 숫자로 채우기(시간 복잡도 n^2)
    for i in range(n):
        for j in range(n):
            arr[i][j] = max(i,j)+1
            
    # 2차원 배열 1차원 배열로 만들기
    arr = sum(arr, [])
    
    # 배열 자르기
    answer = arr[left:right+1]
    return answer
"""