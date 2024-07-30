def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_cnt = [0 for x in range(6)]
    result = 0
    for d in dice:
        dice_cnt[d-1] += 1
    print(dice_cnt)
    
    # 4개다 같을 때
    if max(dice_cnt) == 4:
        result = (dice_cnt.index(max(dice_cnt))+1) * 1111
    # 3개 다 같을 때
    elif max(dice_cnt) == 3:
        result = (10*(dice_cnt.index(3)+1) + (dice_cnt.index(1)+1))**2
    # 2개, 2개씩 같을때
    elif dice_cnt.count(2) == 2:
        num1 = dice_cnt.index(2)+1
        dice_cnt[dice_cnt.index(2)] = 0
        result = (num1 + (dice_cnt.index(2)+1)) * abs(num1 - (dice_cnt.index(2)+1))
    # 2개, 1개, 1개씩 같을떼
    elif dice_cnt.count(1) == 2:
        num1 = dice_cnt.index(1)+1
        dice_cnt[dice_cnt.index(1)] = 0
        result = num1 * (dice_cnt.index(1)+1)
    else:
        result = dice_cnt.index(1) + 1
    return result