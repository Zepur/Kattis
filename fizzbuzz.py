import sys


def solve(n):
    nums = [int(j) for j in n.split()]
    for m in range(1, nums[2]+1):
        if m % nums[0] == 0:
            if m % nums[1] == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif m % nums[1] == 0:
            print('Buzz')
        else:
            print(str(m))


for i in sys.stdin:
    solve(i)
