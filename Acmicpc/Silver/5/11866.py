n, k = map(int, input().split())
chk = [i+1 for i in range(n)]
pos = -1

print('<', end='')

for i in range(n):
    pos += k
    if pos >= len(chk):
        pos = pos % len(chk)
    if i < n-1:
        print(chk.pop(pos), end=', ')
    else:
        print(chk.pop(pos), end='')
    pos -= 1

print('>')
