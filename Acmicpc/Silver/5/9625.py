k = int(input())
s = {'A': 1, 'B': 0}

for _ in range(k):
    a = s['A']
    b = s['B']
    s['A'] = b
    s['B'] = a + b

print(s['A'], s['B'])
