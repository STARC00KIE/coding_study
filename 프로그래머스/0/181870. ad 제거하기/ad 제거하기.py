def solution(strArr):
    for word in strArr[:]:
        if "ad" in word:
            strArr.remove(word)
    return strArr