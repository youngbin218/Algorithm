# 1.
import sys

log = {}
n = int(input())

for _ in range(n):
    name, rec = sys.stdin.readline().rstrip().split()
    if rec == 'enter':
        log[name] = 1
    elif rec == 'leave':
        log[name] = 0

log = sorted(log.items(), reverse=True)

for l in log:
    if l[1] == 1:
        print(l[0])
        
# 2.
import sys

log = {}
n = int(input())

for _ in range(n):
    name, rec = sys.stdin.readline().rstrip().split()
    if rec == 'enter':
        log[name] = 1
    elif rec == 'leave':
        del log[name]

log = sorted(log, reverse=True)

print(*log, sep='\n')
