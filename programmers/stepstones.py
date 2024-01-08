import heapq
from math import inf


def solution(stones, k):
    heap = []
    answer = inf

    for i in range(k-1):
        heapq.heappush(heap, [-stones[i], i])

    for i in range(k-1, len(stones)):
        heapq.heappush(heap, [-stones[i], i])
        while heap[0][1] <= i-k:
            heapq.heappop(heap)
        answer = min(answer, -heap[0][0])

    return answer


print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
