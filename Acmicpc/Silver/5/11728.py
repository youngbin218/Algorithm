# 1.
import sys

n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
idx_a = 0
idx_b = 0

while idx_a != n and idx_b != m:
    if a[idx_a] < b[idx_b]:
        print(a[idx_a], end=' ')
        idx_a += 1
    else:
        print(b[idx_b], end=' ')
        idx_b += 1

if idx_a == n:
    for i in range(idx_b, m):
        print(b[i], end=' ')
elif idx_b == m:
    for i in range(idx_a, n):
        print(a[i], end=' ')

# 2.
import sys

n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
idx_a = 0
idx_b = 0

while idx_a != n or idx_b != m:
    if idx_a == n:
        print(b[idx_b], end=' ')
        idx_b += 1
    elif idx_b == m:
        print(a[idx_a], end=' ')
        idx_a += 1
    else:
        if a[idx_a] < b[idx_b]:
            print(a[idx_a], end=' ')
            idx_a += 1
        else:
            print(b[idx_b], end=' ')
            idx_b += 1
