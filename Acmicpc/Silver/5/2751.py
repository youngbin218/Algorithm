import sys

n = int(input())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()

for num in nums:
    print(num)
