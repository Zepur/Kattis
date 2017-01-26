time = 0
score = 0
wrongs = {}

while True:
    _input = input()
    if _input == '-1':
        break
    else:
        m, L, result = _input.split()
        _m = int(m)
        wrongs[L] = 0 if L not in wrongs else wrongs.get(L)
        if result == 'wrong':
            wrongs[L] += 20
        elif result == 'right':
            score += 1
            time += (_m + wrongs.get(L)) if wrongs.get(L) is not None else _m

print(score, time)
