import sys

score = []
idx = []
total = 0

for i in range(8):
    n = int(sys.stdin.readline().rstrip())
    score.append([n, i+1])

score.sort(key=lambda x: x[0])

for i in range(1, 6):
    total += score[-i][0]
    idx.append(score[-i][1])

idx.sort()

print(total)

for i in idx:
    print(i, end=' ')
