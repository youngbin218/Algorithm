import sys

n, k = input().split()

a = sys.stdin.readline().rstrip()
a = list(map(int, a.split()))

a.sort()

print(a[int(k)-1])
