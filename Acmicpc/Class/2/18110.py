import sys

input = sys.stdin.readline

def n_round(val):
    return round(val+10**(-len(str(val))-1))

n = int(input())

if n == 0:
    print(0)
else:
    num = [int(input()) for i in range(n)]
    num.sort()

    cnt = n_round(n*0.15)

    if cnt != 0:
        num = num[cnt:-cnt]

    print(n_round(sum(num)/(n-2*cnt)))
