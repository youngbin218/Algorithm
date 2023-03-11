import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if (0 <= ax < M) and (0 <= ay < N):
                if box[ay][ax] == 0:
                    box[ay][ax] = box[y][x] + 1
                    q.append((ay, ax))

    res = -2
    for i in range(N):
        for j in range(M):
            if res < box[i][j]:
                res = box[i][j]
            if box[i][j] == 0:
                return -1

    return res - 1

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
chk, res = 0, -1

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
        if box[i][j] == 0:
            chk += 1

if chk == 0:
    print('0')
else:
    print(bfs())
