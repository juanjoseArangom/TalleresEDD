import heapq

ms = int(input())
N = int(input())
heap = []

for _ in range(N):
    tono, mss, fre = map(int, input().split())
    while mss <= ms:
        heapq.heappush(heap, mss)
        mss += fre  
while heap:
    momento = heapq.heappop(heap)
    print(momento)
