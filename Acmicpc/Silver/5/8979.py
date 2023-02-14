import sys

n, c = map(int, input().split())
cs = []
rk = 1

for _ in range(n):
    i, g, s, b = map(int, sys.stdin.readline().rstrip().split())
    if i != c:
        cs.append([g, s, b])
    else:
        tr = [g, s, b]

for s in cs:
    if s[0] > tr[0]:
        rk += 1
    elif s[0] == tr[0]:
        if s[1] > tr[1]:
            rk += 1
        elif s[1] == tr[1]:
            if s[2] > tr[2]:
                rk += 1

print(rk)
