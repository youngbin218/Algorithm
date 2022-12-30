cchk_num = [0] * 10000
cnt = 0

for i in range(1, 10001):
    a = i // 10000 % 10
    b = i // 1000 % 10
    c = i // 100 % 10
    d = i // 10 % 10
    e = i % 10
    total = i+a+b+c+d+e
    if total-1 < 10000 and chk_num[total-1] == 0:
        chk_num[total-1] = 1
        
for i in range(10000):
    if chk_num[i] == 0:
        print(i+1)
