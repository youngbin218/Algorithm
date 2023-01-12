import sys

n = int(input())
mems = []

for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    mems.append([int(age), name, i])

mems.sort(key=lambda x: (x[0], x[2]))

for m in mems:
    print(m[0], m[1])
