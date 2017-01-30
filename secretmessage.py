import math

N = int(input())


def rotate_clockwise(matrix, degree=90):
    return matrix if not degree else rotate_clockwise(zip(*matrix[::-1]), degree - 90)


for i in range(N):
    secret = input()
    _k = math.sqrt(len(secret))
    K = int(_k) if _k == int(_k) else int(_k) + 1
    letters = [['*' for _ in range(K)] for _ in range(K)]
    its = 0
    for x in range(K):
        for y in range(K):
            if its + 1 <= len(secret):
                letters[x][y] = (secret[its])
            else:
                break
            its += 1
    coded = ''.join([s for _s in rotate_clockwise(letters) for s in _s if s != '*'])

    print(coded)
