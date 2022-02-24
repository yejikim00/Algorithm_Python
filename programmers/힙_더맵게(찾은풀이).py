import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
        else:
            answer = -1
            return answer
    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))