import sys

sys.setrecursionlimit(10000000)

def dfs(x, y):
    visited[x][y] = 1
    color = pic[x][y]

    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if (0 <= ax < n) and (0 <= ay < n):
            if visited[ax][ay] == 0 and pic[ax][ay] == color:
                dfs(ax, ay)

n = int(input())
pic = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

region, blind_region = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            region += 1

for i in range(n):
    for j in range(n):
        if pic[i][j] == 'G':
            pic[i][j] = 'R'

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            blind_region += 1
