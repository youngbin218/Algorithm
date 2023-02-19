import sys

n, k = map(int, input().split())
bag = []
val = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split())
    bag.append([w, v])

bag.sort(key=lambda x: (x[0], x[1]))

for i in range(1, n+1):
    for j in range(1, k+1):
        if bag[i-1][0] > j:
            val[i][j] = val[i-1][j]
        else:
            val[i][j] = max(val[i-1][j], val[i-1][j-bag[i-1][0]] + bag[i-1][1])

print(val[n][k])
