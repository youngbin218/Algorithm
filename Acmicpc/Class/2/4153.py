import sys

input = sys.stdin.readline

in_list = []

while True:
    a, b, c = input().rstrip().split()
    if a == '0' and b == '0' and c == '0':
        break
    else:
        in_list.append(list(map(int, (a, b, c))))
        
for i in in_list:
    c_i = i.index(max(i))
    tmp = i[c_i]
    i[c_i] = i[2]
    i[2] = tmp
    if i[0]**2 + i[1]**2 == i[2]**2:
        print('right')
    else:
        print('wrong')
