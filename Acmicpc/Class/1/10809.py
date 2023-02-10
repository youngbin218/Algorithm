import sys

s = sys.stdin.readline().rstrip()
chk_idx = {}

for idx, i in enumerate(s):
    if i not in chk_idx:
        chk_idx[i] = idx

for i in range(97, 123):
    alphabet = chr(i)
    if alphabet not in chk_idx:
        print(-1, end=' ')
    else:
        print(chk_idx[alphabet], end=' ')
