e, s, m = map(int, input().split())
year = 1

while 1:
    if e != 1:
        tmp = e - 1
        e = 1
        s -= tmp
        m -= tmp
        year += tmp
    elif s == 1 and m == 1:
        break
    else:
        s -= 15
        m -= 15
        year += 15
    if s <= 0:
        s += 28
    if m <= 0:
        m += 19

print(year)
