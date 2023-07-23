import sys

input = sys.stdin.readline

n = int(input())

line = [int(input()) for _ in range(n)]
chk = []
res = []
loc = 1

for j in range(n):
    i = 1
    while i <= n:
        if i < loc:
            if i != line[j] and line[j-1] < line[j]:
                i = loc - 1
            else:
                if line[j] == chk[-1]:
                    res.append('-')
                    chk = chk[:-1]
                    break
                else:
                    print('NO')
                    exit()
        else:
            loc += 1
            if i == line[j]:
                res.append('+')
                res.append('-')
                break
            else:
                res.append('+')
                chk.append(i)
        i += 1

for oper in res:
    print(oper)
