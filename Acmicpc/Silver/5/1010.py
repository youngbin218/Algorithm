import sys

t = int(input())
bridges = []

def combination(n, r):
    if n == r or r == 0:
        return 1
    arr = [[0] * 29 for i in range(29)]
    for i in range(n):
        for j in range(i+1):
            if i == j or j == 0:
                arr[i][j] = 1
            elif i > 0 and j > 0:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr[n-1][r] + arr[n-1][r-1]

for i in range(t):
    b = sys.stdin.readline().rstrip()
    bridges.append(list(map(int, b.split())))

for b in bridges:
    print(combination(b[1], b[0]))
