import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coin = [int(input().rstrip()) for _ in range(n)]
val = [0] * (k+1)

val[0] = 1

for i in range(n):
    for j in range(coin[i], k+1):
        val[j] += val[j-coin[i]]

print(val[k])
