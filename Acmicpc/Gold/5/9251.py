str_1 = input()
str_2 = input()

n = len(str_1) + 1
m = len(str_2) + 1

lcs = [[0] * n for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        if str_2[i-1] == str_1[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[m-1][n-1])
