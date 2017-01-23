import sys


def compute(s):
    nums = [int(n) for n in s.split()]
    print(abs(nums[0] - nums[1]))


for i in sys.stdin:
    compute(i)
