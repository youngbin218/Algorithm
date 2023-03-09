import sys

input = sys.stdin.readline

N = int(input())
cnt, num = 0, 1

while 1:
    if N <= num + cnt * 6:
        break
    else:
        num += cnt * 6
        cnt += 1

print(cnt+1)
