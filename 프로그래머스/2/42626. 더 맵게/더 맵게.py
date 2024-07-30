import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while K > scoville[0]:
        if len(scoville) == 1:
            return -1
        result1 = heapq.heappop(scoville)
        result2 = heapq.heappop(scoville)
    
        tmp = result1 + result2 * 2
        heapq.heappush(scoville, tmp)
        cnt +=1
    
    return cnt