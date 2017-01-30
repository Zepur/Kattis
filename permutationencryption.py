res = []

while True:
    _in = input()
    if _in == '0':
        break
    _input = [int(j) for j in _in.split()]
    N = int(_input[0])
    key = [_input[j] for j in range(1, len(_input))]
    message = input()

    while len(message) % N != 0:
        message += ' '

    new_word = ''
    _k = 0
    _s = 0

    while len(new_word) < len(message):
        new_word += message[key[_k] - 1 + _s]
        _k += 1
        if _k == N:
            _k = 0
            _s += N
    res.append(new_word)

for x in res:
    print('\'' + x + '\'')
