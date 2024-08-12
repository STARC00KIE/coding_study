def solution(name):
    # 1. 알파벳 조작 횟수 계산
    def min_jostick_moves(char):
        diff = ord(char) - ord('A')
        return min(diff, 26 - diff)
    
    # 2. 알파벳 조작 횟수 총합 계산
    total_moves = sum(min_jostick_moves(char) for char in name)
    
    # 3. 커서 이동을 위한 최소 이동 계산
    n = len(name)
    min_cursor_moves = n - 1  # 최악의 경우, 모든 문자를 오른쪽으로 이동
    
    # 4. 각 문자의 'A' 사이 거리 계산
    for i in range(n):
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        
        # 커서가 i 위치에서 next_index로 이동할 경우 거리 계산
        distance = 2 * i + (n - next_index)
        min_cursor_moves = min(min_cursor_moves, distance)
        
        distance = 2 * (n - next_index) + i
        min_cursor_moves = min(min_cursor_moves, distance)
    
    return total_moves + min_cursor_moves