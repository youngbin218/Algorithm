import sys

input = sys.stdin.readline

a, b, v = input().split()
d = int(a) - int(b)
z = int(v) - int(a)

res = z // d if z % d == 0 else z // d + 1

print(res+1)
