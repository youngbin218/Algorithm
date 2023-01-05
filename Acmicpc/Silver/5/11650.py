import sys

n = int(input())
points = []

for i in range(n):
    p = sys.stdin.readline().rstrip()
    points.append(list(map(int, p.split())))

points.sort(key=lambda x: (x[0], x[1]))

for p in points:
    print(p[0], p[1])
