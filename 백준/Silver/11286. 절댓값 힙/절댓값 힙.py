import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))
    
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
