import sys

n = int(input())
students = []
rank = [1] * n

for i in range(n):
    val = sys.stdin.readline().rstrip()
    students.append(list(map(int, val.split())))

for i in range(n):
    for j in range(n):
        if students[i][0] < students[j][0] and students[i][1] < students[j][1]:
            rank[i] += 1

for rk in rank:
    print(rk, end=' ')
