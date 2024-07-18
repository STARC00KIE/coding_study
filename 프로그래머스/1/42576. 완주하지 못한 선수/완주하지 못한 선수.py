"""
def solution(participant, completion):
    for comp in completion:
        participant.remove(comp)
        
    answer = participant.pop(0)
    return answer
"""

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant[-1]
