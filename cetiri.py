nums = [int(i) for i in input().split()]
nums.sort()

if abs(nums[0] - nums[1]) > abs(nums[1] - nums[2]):
    print(nums[0] + abs(nums[2] - nums[1]))
elif abs(nums[0] - nums[1]) < abs(nums[1] - nums[2]):
    print(nums[1] + abs(nums[0] - nums[1]))
else:
    print(nums[2] + abs(nums[1] - nums[2]))
