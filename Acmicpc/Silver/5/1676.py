n = int(input())
fac = 1
cnt = 0

for i in range(1, n + 1):
    fac = fac * i

fac = str(fac)

for i in range(len(fac)):
    if fac[-(i+1)] == '0':
        cnt += 1
    else:
        break

print(cnt)
