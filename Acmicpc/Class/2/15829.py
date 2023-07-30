import sys

input = sys.stdin.readline

L = int(input())
strs = input()

total = 0

for i in range(L):
    total += (ord(strs[i]) - 96) * (31**i)

print(total % 1234567891)
