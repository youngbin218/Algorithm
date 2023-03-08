import sys

input = sys.stdin.readline

N = int(input())
n = N // 5
cnt = 10000

for i in range(n, -1, -1):
    tmp = N - 5 * i
    if tmp % 3 == 0:
        cnt = min(cnt, i+tmp//3)

if cnt == 10000:
    cnt = -1

print(cnt)
