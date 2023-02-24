import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(c_h):
    m_dist = 100
    dist = 0
    total = 0
    for l in loc_h:
        for c in c_h:
            dist = abs(c[0]-l[0]) + abs(c[1]-l[1])
            if dist < m_dist:
                m_dist = dist
        total += m_dist
        m_dist = 100
    
    return total

n, m = map(int, input().rstrip().split())
c = [list(map(int, input().rstrip().split())) for _ in range(n)]
loc_h = []
loc_c_h = []
c_dist = 10000

for i in range(n):
    for j in range(n):
        if c[i][j] == 1:
            loc_h.append([i, j])
        if c[i][j] == 2:
            loc_c_h.append([i, j])

loc_c_h = list(combinations(loc_c_h, m))

for c_h in loc_c_h:
    res = dfs(c_h)
    if res < c_dist:
        c_dist = res

print(c_dist)
