str = input()
answer = ''
for i in range(len(str)):
    if str[i] == str[i].upper(): # 대문자일때
        answer += str[i].lower()
    else:
        answer += str[i].upper()
        
print(answer)