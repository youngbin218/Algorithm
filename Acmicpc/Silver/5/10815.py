# 1. set
import sys

n = int(input())
num = sys.stdin.readline().rstrip().split()
ns = set(map(int, num))

m = int(input())
num = sys.stdin.readline().rstrip().split()
ms = list(map(int, num))

for m in ms:
    if m in ns:
        print('1', end=' ')
    else:
        print('0', end=' ')
        
# 2. Binary Search
import sys

n = int(input())
num = sys.stdin.readline().rstrip().split()
ns = list(map(int, num))

m = int(input())
num = sys.stdin.readline().rstrip().split()
ms = list(map(int, num))

ns.sort()

for i in range(m):
    l = 1
    r = len(ns)
    while 1:
        if l > r:
            print('0', end=' ')
            break
        idx = (l+r) // 2
        if ns[idx-1] == ms[i]:
            print('1', end=' ')
            break
        elif ns[idx-1] > ms[i]:
            r = idx - 1
        else:
            l = idx + 1
