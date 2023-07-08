import sys

input = sys.stdin.readline

N = int(input())
h_card = list(map(int, input().split()))
M = int(input())
c_card = list(map(int, input().split()))
chk = {}

for h in h_card:
    if h not in chk:
        chk[h] = 1
    else:
        chk[h] += 1

for c in c_card:
    if c not in chk:
        print('0', end=' ')
    else:
        print(chk[c], end=' ')
