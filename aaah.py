import sys


def solve(s_1, s_2):
    print('go' if len(s_1) >= len(s_2) else 'no')

inp_1 = None
inp_2 = None

for i in sys.stdin:
    if inp_1 is None:
        inp_1 = i
    elif inp_2 is None:
        inp_2 = i
        solve(inp_1, inp_2)
        inp_1 = None
        inp_2 = None

