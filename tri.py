a, b, c = [int(i) for i in input().split()]


def _sum(_1, _2, _3):
    if _1 + _2 == _3:
        return '+'
    elif _1 - _2 == _3:
        return '-'
    elif _1 / _2 == _3:
        return '/'
    elif _1 * _2 == _3:
        return '*'
    else:
        return '!'


_c = _sum(a, b, c)
_a = _sum(b, c, a)
if _a in ('-', '+', '/', '*'):
    print(str(a) + '=' + str(b) + _a + str(c))
else:
    print(str(a) + _c + str(b) + '=' + str(c))
