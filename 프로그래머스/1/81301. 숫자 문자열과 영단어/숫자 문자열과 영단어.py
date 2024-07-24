def solution(s):
    dic = {'zero': '0', 'one': '1','two': '2', 'three': '3', 'four': '4', 'five': '5', 'six':'6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = ""
    numstr = ""
    for c in s:
        # 숫자일 때
        try:
            int(c)
            answer += c
            
        # 문자일 때
        except:
            numstr += c
            try:
                answer += dic[numstr]
                numstr = "" 
            except:
                pass
    return int(answer)