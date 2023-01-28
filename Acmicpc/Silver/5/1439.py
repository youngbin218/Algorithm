import sys

s = sys.stdin.readline().rstrip()
cnt = [0, 0]

for i in range(len(s)):
    if i >= 1:
        if s[i] != s[i-1]:
            cnt[int(s[i-1])] += 1
cnt[int(s[-1])] += 1

print(min(cnt[0], cnt[1]))
