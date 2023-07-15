import sys

input = sys.stdin.readline

def prime(n):
    tmp = 2
    while n * tmp <= int(M):
        num[n*tmp] = False
        tmp += 1

N, M = input().split()
num = [True] * (int(M)+1)
num[0] = False
num[1] = False

for i in range(2, int(M)+1):
    if num[i] == True:
        prime(i)

for i in range(int(M)+1):
    if num[i] and i >= int(N):
        print(i)
