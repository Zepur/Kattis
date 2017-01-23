chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
_output = []

while True:
    _input = input()
    if _input == '0':
        for _o in _output:
            print(_o)
        quit()
    else:
        N, s = _input.split()
        _encrypt = ''
        for c in s:
            _encrypt += chars[int(N) + chars.index(c)]
        print(_encrypt[::-1])
