def solution(record):
    uid_dic = {}  # 유저 아이디와 이름을 매핑하는 딕셔너리
    answer = []  # 최종 결과를 담을 리스트

    # record의 각 라인을 처리
    for line in record:
        tmp = line.split()
        
        # ENTER일 때
        if tmp[0] == 'Enter':
            uid_dic[tmp[1]] = tmp[2]  # 딕셔너리에 유저 업데이트
            answer.append((tmp[1], "님이 들어왔습니다."))  # 기록 저장

        # LEAVE일 때
        if tmp[0] == 'Leave':
            answer.append((tmp[1], "님이 나갔습니다."))  # 기록 저장

        # CHANGE일 때
        if tmp[0] == 'Change':
            uid_dic[tmp[1]] = tmp[2]  # 닉네임 업데이트

    # 유저 아이디를 닉네임으로 바꾸기
    result = []
    for uid, action in answer:
        result.append(f"{uid_dic[uid]}{action}")

    return result