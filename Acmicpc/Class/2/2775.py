import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    h = [[0] * n for j in range(k+1)]
    for j in range(n):
        h[0][j] = j + 1
    for j in range(1, k+1):
        total = 0
        for x in range(n):
            total += h[j-1][x]
            h[j][x] = total

    print(h[k][n-1])
