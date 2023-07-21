import sys

input = sys.stdin.readline

K = int(input())
num = []

for i in range(K):
    n = int(input())
    num.pop() if n == 0 else num.append(n)
