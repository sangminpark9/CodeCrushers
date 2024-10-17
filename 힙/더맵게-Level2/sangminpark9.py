import heapq

def solution(scoville, K):
    answer = 0
    if len(scoville) <= 1:
        return -1
    heapq.heapify(scoville)
    
    while scoville[0] < K: # 제일 작은 값도 K이상이면 다 K 이상
        if len(scoville) <= 1:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (min1 + (2 * min2)))
        answer += 1

    return answer
