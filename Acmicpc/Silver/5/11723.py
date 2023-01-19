import sys

n = int(input())
opers = []
a = set()

for i in range(n):
    oper = sys.stdin.readline().rstrip()
    if oper != 'all' and oper != 'empty':
        oper, num = oper.split()
        num = int(num)

    if oper == 'add':
        if num not in a:
            a.add(num)
    elif oper == 'remove':
        if num in a:
            a.remove(num)
    elif oper == 'check':
        print(1 if num in a else 0)
    elif oper == 'toggle':
        if num in a:
            a.remove(num)
        else:
            a.add(num)
    elif oper == 'all':
        a = set({i + 1 for i in range(20)})
    elif oper == 'empty':
        a.clear()
