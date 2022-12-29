import math

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

def prime_number(num):
    if num == 1:
        return False
    else :
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return 0
        return 1

for idx in range(n):
    cnt += prime_number(nums[idx])

print(cnt)