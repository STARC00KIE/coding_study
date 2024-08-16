def solution(strArr):
    for i, st in enumerate(strArr):
        if (i+1) % 2 == 1:
            strArr[i] = st.lower()
        else:
            strArr[i] = st.upper()
    return strArr