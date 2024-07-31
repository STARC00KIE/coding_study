import heapq

def solution(operations):
    heap = []
    
    for o in operations:
        if o[0] == "I":
            heapq.heappush(heap, int(o[2:]))
        
        elif o[0] == "D": # else로 처리 가능
            if len(heap) == 0:
                pass
            elif o[2:] == "1":
                # 최대값 삭제
                max_val = heapq.nlargest(1, heap)[0]
                heap.remove(max_val)
                heapq.heapify(heap)
                
            else:
                heapq.heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap),min(heap)]