current = int(input())
target = int(input())


def find_cw():
    _start = current
    moved = 0
    while _start != target:
        _start += 1
        moved += 1
        if _start == 360:
            _start = 0
    return moved


def find_ccw():
    _start = current
    moved = 0
    while _start != target:
        _start -= 1
        moved -= 1
        if _start == -1:
            _start = 359
    return moved


ccw = find_ccw()
cw = find_cw()
x = str(ccw) if abs(ccw) < abs(cw) else str(cw)
print(x)
