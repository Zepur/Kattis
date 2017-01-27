N = int(input())


def get_operators():
    n = ['*', '+', '-', '/']
    _n = []
    for x in n:
        for y in n:
            for z in n:
                _n.append([x, y, z])
    return _n


def calc(ans):
    _s = None
    _op = get_operators()
    for j in _op:
        if len(j) <= 0:
            break
        else:
            num = [4, 4, 4, 4]
            __j = j.copy()
            if '/' in j or '*' in j:
                roof = len(j) - (str(j).count('/') + str(j).count('*'))
                _i = 0
                while len(j) > roof:
                    if j[_i] == '*':
                        num[_i] *= num[_i + 1]
                        num = [l for l in num[0:_i+1]] + [l for l in num[_i+2:]]
                        del j[_i]
                    elif j[_i] == '/':
                        num[_i] //= num[_i + 1]
                        num = [l for l in num[0:_i+1]] + [l for l in num[_i + 2:]]
                        del j[_i]
                    else:
                        _i += 1
                _i = 0
                while len(j) > 0:
                    if j[_i] == '+':
                        num[_i] += num[_i+1]
                        num = [l for l in num[0:_i+1]] + [l for l in num[_i + 2:]]
                        del j[_i]
                    elif j[_i] == '-':
                        num[_i] -= num[_i+1]
                        num = [l for l in num[0:_i+1]] + [l for l in num[_i + 2:]]
                        del j[_i]
                _a = num[0]
                if _a == ans:
                    _s = '4 %s 4 %s 4 %s 4 = %s' % (__j[0], __j[1], __j[2], _a)
            else:
                s = '4 ' + j[0] + ' 4 ' + j[1] + ' 4 ' + j[2] + ' 4'
                _a = int(eval(s))
                if _a == ans:
                    _s = '4 %s 4 %s 4 %s 4 = %s' % (__j[0], __j[1], __j[2], _a)
    if _s:
        return _s
    else:
        return 'no solution'


ansis = []


for i in range(N):
    inp = int(input())
    if -61 < inp < 257:
        ansis.append(calc(inp))
    else:
        ansis.append('no solution')
else:
    for k in ansis:
        print(k)
