n = int(input())
nums = {}

while n != 0:
    val = n % 10
    if val in nums:
        nums[val] += 1
    else:
        nums[val] = 1
    n = n // 10

if 6 in nums and 9 in nums:
    a = nums[6]
    b = nums[9]
    if a > b:
        nums[6] = b + (a-b+1) // 2
    elif a < b:
        nums[9] = a + (b-a+1) // 2
elif 6 in nums and 9 not in nums:
    nums[6] = (nums[6]+1) // 2
elif 6 not in nums and 9 in nums:
    nums[9] = (nums[9]+1) // 2

nums = dict(sorted(nums.items(), reverse=True, key=lambda x: x[1]))

print(list(nums.values())[0])
