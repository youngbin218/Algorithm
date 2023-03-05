import sys
import math
import heapq

input = sys.stdin.readline

def Dijkstra(start):
    d[start-1] = 0
    
    hq = []
    heapq.heappush(hq, (start, 0))
    
    while len(hq) != 0:
        tr_c, cost = heapq.heappop(hq)
        if d[tr_c-1] < cost:
            continue
            
        for b in bus[tr_c-1]:
            if d[tr_c-1] + b[1] < d[b[0]-1]:
                heapq.heappush(hq, (b[0], b[1]))
                d[b[0]-1] = d[tr_c-1] + b[1]

    return d[e_c-1]

n = int(input())
m = int(input())
bus = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a-1].append((b, c))

s_c, e_c = map(int, input().split())

d = [math.inf for _ in range(n)]

print(Dijkstra(s_c))
