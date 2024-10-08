def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    l = len(citations)
    
    for i in range(l): # 0 ~ 4
        h = i + 1
        if h <= citations[i]:
            answer = h
        else:
            break
    return answer
