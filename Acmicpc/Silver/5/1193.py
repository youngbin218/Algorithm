x = int(input())
chk = 0
idx = 0

while chk < x:
    idx += 1
    chk = (idx*(idx+1)) // 2

chk = x - ((idx-1)*idx) // 2

if idx % 2 == 0:
    print(f"{chk}/{idx+1-chk}")
else:
    print(f"{idx+1-chk}/{chk}")
