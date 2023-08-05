import sys

input = sys.stdin.readline

a, b = input().split()

a = int(a)
b = int(b)
idx = 0
t = 1
res = 0
r = 999

while t != 0:
    idx += 1
    t = max(a, b) * idx % min(a, b)
    res = max(a, b) * idx

while r != 0:
    r = max(a, b) % min(a, b)
    if a > b:
        a = r
    else:
        b = r

print(max(a, b))
print(res)
