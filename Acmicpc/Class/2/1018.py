import sys

input = sys.stdin.readline

N, M = input().split(' ')
N = int(N)
M = int(M)
chess = [input() for _ in range(N)]

pattern_1 = "WBWBWBWB"
pattern_2 = "BWBWBWBW"

res = 33

for i in range(N):
    for j in range(M):
        pattern_1_cnt = 0
        pattern_2_cnt = 0
        if i + 8 <= N and j + 8 <= M:
            for k in range(8):
                for q in range(8):
                    if (i+k) % 2 == 0:
                        if chess[i+k][j+q] is pattern_1[q]:
                            pattern_2_cnt += 1
                        if chess[i+k][j+q] is pattern_2[q]:
                            pattern_1_cnt += 1
                    else:
                        if chess[i+k][j+q] is pattern_1[q]:
                            pattern_1_cnt += 1
                        if chess[i+k][j+q] is pattern_2[q]:
                            pattern_2_cnt += 1
            pattern_1_cnt = min(pattern_1_cnt, pattern_2_cnt)
            res = min(res, pattern_1_cnt)
print(res)
