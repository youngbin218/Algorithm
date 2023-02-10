import sys

t = int(input())

for _ in range(t):
    r, ss = sys.stdin.readline().rstrip().split()
    for s in ss:
        print(s * int(r), end='')
    print()
