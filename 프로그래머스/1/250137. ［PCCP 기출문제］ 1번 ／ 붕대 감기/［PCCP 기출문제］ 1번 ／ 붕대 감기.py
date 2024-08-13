def solution(bandage, health, attacks):
    time = attacks[-1][0]
    dic = dict(attacks)
    maxhealth = health
    cnt = 0
    for t in range(time):
    
        if t + 1 in dic: # 공격시간일 때
            health -= dic[t+1]
            cnt = 0
            if health <= 0:
                return -1
        else: # 공격 없을 때
            cnt += 1
            health += bandage[1]
            
            if cnt == bandage[0]:
                health += bandage[2]
                cnt = 0
            
            if health > maxhealth:
                health = maxhealth
        print(f't: {t+1}, health: {health}, cnt: {cnt}')
    return health
        
            