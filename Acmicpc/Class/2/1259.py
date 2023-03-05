import sys

input = sys.stdin.readline

while 1:
    n = input().rstrip()
    if n == '0':
        break
    else:
        if n == n[::-1]:
            print('yes')
        else:
            print('no')
