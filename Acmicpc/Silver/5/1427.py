import math

num = int(input())
ns = []
result = 0

for i in range(len(str(num))):
    ns.append(num // math.pow(10, i) % 10)

ns.sort()

for idx, n in enumerate(ns):
    result += n * math.pow(10, idx)

print(int(result))
