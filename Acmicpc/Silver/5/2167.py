import sys

n, m = map(int, input().split())
arr = []

for i in range(n):
    ns = sys.stdin.readline().rstrip()
    arr.append(list(map(int, ns.split())))

for i in range(m):
    for j in range(n):
        if j >= 1:
            arr[j][i] += arr[j-1][i]

k = int(input())

for i in range(k):
    res = 0
    s = sys.stdin.readline().rstrip()
    s = list(map(int, s.split()))
    for j in range(s[1]-1, s[3]):
        if s[0] > 1:
            res += arr[s[2]-1][j] - arr[s[0]-2][j]
        else:
            res += arr[s[2]-1][j]
    print(res)
