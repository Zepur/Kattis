from itertools import groupby as g

name = list(input())
print(''.join(c for c, _ in g(name)))
