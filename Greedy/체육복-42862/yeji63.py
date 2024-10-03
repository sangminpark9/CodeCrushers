def solution(n, lost, reserve):
    answer = 0
    
    lost_a = [l for l in lost if l not in reserve]
    reserve_a = [r for r in reserve if r not in lost]
    
    for r in sorted(reserve_a):
        if r-1 in lost_a:
            lost_a.remove(r-1)
        elif r+1 in lost_a:
            lost_a.remove(r+1)
            
    answer = n - len(lost_a)
    
    return answer
