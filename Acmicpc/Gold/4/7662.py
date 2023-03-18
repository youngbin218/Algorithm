import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    i, d1, d2 = 0, 0, 0
    hq_min = []
    hq_max = []
    chk = {}
    for _ in range(k):
        s, n = input().split()
        n = int(n)
        if s == 'I':
            heapq.heappush(hq_min, n)
            heapq.heappush(hq_max, (-n, n))
            if n in chk:
                chk[n] += 1
            else:
                chk[n] = 1
            i += 1
        if s == 'D':
            if i == d1 + d2:
                continue
            if n == 1:
                while 1:
                    tmp = heapq.heappop(hq_max)[1]
                    if chk[tmp] > 0:
                        chk[tmp] -= 1
                        break
                d1 += 1
            if n == -1:
                while 1:
                    tmp = heapq.heappop(hq_min)
                    if chk[tmp] > 0:
                        chk[tmp] -= 1
                        break
                d2 += 1

    if i == d1 + d2:
        print('EMPTY')
    else:
        val = [k for k, v in chk.items() if v > 0]
        print(f'{max(val)} {min(val)}')
