pieces = [1, 1, 2, 2, 2, 8]
what_i_got = [int(n) for n in input().split()]
summy = [a - b for a, b in zip(pieces, what_i_got)]

print(' '.join(str(b) for b in summy))
