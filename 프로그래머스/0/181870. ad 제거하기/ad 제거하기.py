def solution(strArr):
    for word in strArr[:]: # [:] => 데이터 복사해서 사용
        if "ad" in word:
            strArr.remove(word)
    return strArr