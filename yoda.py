N = input()
M = input()


def justify(s, l):
    _s = s.rjust(l, '0')
    return reversed(_s)

man_len = max(len(N), len(M))
_N = list(justify(N, man_len))
_M = list(justify(M, man_len))

for i in range(len(_N)):
    if int(_N[i]) > int(_M[i]):
        _N[i] = _N[i]
        _M[i] = '_'
    elif int(_M[i]) > int(_N[i]):
        _M[i] = _M[i]
        _N[i] = '_'
    elif int(_N[i]) == int(_M[i]):
        continue


def is_yoda(_s):
    _s = _s.replace('_', '')
    if len(_s) == 0:
        return 'YODA'
    else:
        if len(_s.replace('0', '')) == 0:
            return '0'
        return reversed(_s)


_N = is_yoda(''.join(s for s in _N))
_M = is_yoda(''.join(s for s in _M))

print(''.join(s for s in _N if s != '_'))
print(''.join(s for s in _M if s != '_'))
