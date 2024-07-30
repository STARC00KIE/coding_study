def solution(rsp):
    answer = ""
    winrsp = {'2' : '0', '0' : '5', '5' : '2'}
    for s in rsp:
        answer += winrsp[s]
    return answer