import sys

a = []
b = []

n, m = map(int, input().split())
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))

m, k = map(int, input().split())
for i in range(m):
    b.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(k):
        tmp = 0
        for l in range(m):
            tmp += a[i][l] * b[l][j]
        if j < k - 1:
            print(tmp, end=' ')
        else:
            print(tmp)
