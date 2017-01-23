import sys

cases = -2
runs = 4


def solve(n):
    global cases, runs
    if runs != 0:
        if runs == -2:
            runs = int(n)
        else:
            print(n.split()[0], 'is even' if abs(int(n)) % 2 == 0 else 'is odd')
            runs -= 1


for i in sys.stdin:
    solve(i)
