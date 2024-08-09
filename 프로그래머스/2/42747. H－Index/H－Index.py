# 8:03

def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if citation <= i:
            return i
    return len(citations)

# i j
# 3 3,0,6,1,5
