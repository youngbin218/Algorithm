import sys

input = sys.stdin.readline

N = int(input())
num = [int(input()) for i in range(N)]
num.sort()
cnt = {}

for n in num:
    if n in cnt:
        cnt[n] += 1
    else:
        cnt[n] = 1

tmp = [k for k, v in cnt.items() if v == max(cnt.values())]

print(round(sum(num) / N))
print(num[N // 2])
print(tmp[0]) if len(tmp) == 1 else print(tmp[1])
print(num[-1] - num[0])
