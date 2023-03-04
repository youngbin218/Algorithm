import sys

input = sys.stdin.readline

N = input().rstrip()
m = int(input().rstrip())
if m != 0:
    s = set(input().rstrip().split())
else:
    s = set()

res = abs(int(N)-100)

for num in range(1000000):
    bool = True
    for n in str(num):
        if n in s:
            bool = False
            break
    if bool:
        tmp = abs(int(N)-num) + len(str(num))
        res = min(res, tmp)

print(res)
