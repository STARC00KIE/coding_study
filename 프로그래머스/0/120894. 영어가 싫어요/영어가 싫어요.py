def solution(numbers):
    numdic = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    
    answer = ""
    strnum = ""
    for n in numbers:
        strnum += n
        if strnum in numdic:
            answer += numdic[strnum]
            strnum = ""
    return int(answer)