def solve(s, used, result):
    # 모든 문자를 다 썼으면 끝!
    if all(used):
        return

    min_str = None
    min_idx = -1

    # 아직 안 쓴 문자 중, 하나씩 추가해서 사전순으로 제일 앞인 걸 고르기
    for i in range(len(s)):
        if not used[i]:
            temp = ""
            for j in range(len(s)):
                if used[j] or j == i:
                    temp += s[j]
            if min_str is None or temp < min_str:
                min_str = temp
                min_idx = i

    # 고른 문자 사용 처리
    used[min_idx] = True
    print(min_str)
    
    # 재귀 호출 (다음 글자 고르러)
    solve(s, used, min_str)

# 입력 처리
s = input()
used = [False] * len(s)
solve(s, used, "")
