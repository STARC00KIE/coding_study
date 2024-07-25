def solution(s):
    s = s.lower()
    answer = ""
    for i in range(len(s)):
        if (i!=0) and s[i-1] == " ": # 글자 숫
            answer += s[i].upper()
        elif (i==0):
            answer += s[i].upper()
        else: # 공백일 때
            answer += s[i]
    return answer