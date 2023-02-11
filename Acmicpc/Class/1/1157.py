word = input().upper()
chk = [[i, 0] for i in range(26)]

for w in word:
    chk[ord(w)-65][1] += 1

chk.sort(key=lambda x: (-x[1], x[0]))

if chk[0][1] == chk[1][1]:
    print('?')
else:
    print(chr(chk[0][0]+65))
