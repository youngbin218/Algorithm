import sys

input = sys.stdin.readline

def AC(p, val):
    cnt, t, b = 0, 0, 0
    le = len(val)
    for f in p:
        if f == 'R':
            cnt += 1
        if f == 'D':
            if le != 0:
                if cnt % 2 == 0:
                    t += 1
                else:
                    b += 1
                le -= 1
            else:
                print('error')
                return

    if le == 0:
        print('[]')
        return
    
    if b == 0:
        val = val[t:]
    else:
        val = val[t:-b]

    print('[', end='')
    for i in range(len(val)-1):
        if cnt % 2 == 0:
            print(f'{val[i]}', end=',')
        else:
            print(f'{val[-i-1]}', end=',')

    if cnt % 2 == 0:
        print(f'{val[-1]}]')
    else:
        print(f'{val[0]}]')

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    val = input().rstrip()
    if val != '[]':
        val = list(map(int,
                       val.strip('['']').split(',')))
    else:
        val = []
    AC(p, val)
