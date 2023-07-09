import sys

input = sys.stdin.readline

N = int(input())
N_num = set(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))

for m in M_num:
    if m in N_num:
        print('1')
    else:
        print('0')
