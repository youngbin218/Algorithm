import math

m = int(input())
n = int(input())
num = []
total = 0

def prime_number(num):
    if num == 1:
        return 0
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return 0
        return 1

for i in range(m, n + 1):
    if prime_number(i):
        num.append(i)
        total += i

if len(num) == 0:
    print(-1)
else:
    print(total)
    print(num[0])
