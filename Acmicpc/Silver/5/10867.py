import sys

n = int(input())
num = list(set(map(int, sys.stdin.readline().rstrip().split())))

num.sort()

for m in num:
    print(m, end=' ')
