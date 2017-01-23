import sys


def solve(s):
    dice = [int(_i) for _i in s.split()]
    if dice[0] == dice[1]:
        print(str(dice[0]+1))
    else:
        diff = abs(dice[0] - dice[1])
        m = min(dice) + 1
        for n in range(m, m + diff + 1):
            print(n)


for i in sys.stdin:
    solve(i)
