str = input()
alphabets = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
i = 0
cnt = 0

while i != len(str):
    if i+2 < len(str) and str[i] + str[i+1] + str[i+2] == 'dz=':
        cnt += 1
        i += 2
    elif i+1 < len(str) and str[i] + str[i+1] in alphabets:
        cnt += 1
        i += 1
    else:
        cnt += 1
    i += 1

print(cnt)
