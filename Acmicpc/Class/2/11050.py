import sys

input = sys.stdin.readline

def fac(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

N, K = input().split()

print(int(fac(int(N)) / (fac(int(K)) * fac(int(N)-int(K)))))
