import sys

N = int(input())

for i in range(N):
    one = input()
    two = input()
    print(one)
    print(two)
    s = ''
    for c in range(len(one)):
        s += '*' if one[c] != two[c] else '.'
    print(s)
