L = int(input())
D = int(input())
X = int(input())
target = X


def get_N():
    for i in range(L, D+1):
        _min = str(i)
        _min_sum = 0
        _min_sum += sum([int(n) for n in _min])
        if _min_sum == X:
            return i


def get_M():
    for i in range(D, L-1, -1):
        _max = str(i)
        _max_sum = sum([int(n) for n in _max])
        if _max_sum == X:
            return i


print(get_N())
print(get_M())
