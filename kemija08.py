vowels = ['a', 'e', 'i', 'o', 'u']

_in = input()
_in = list(_in)

for i in range(len(_in)-2):
    if _in[i] == '.':
        continue
    if _in[i] in vowels and _in[i+1] == 'p' and _in[i+2] == _in[i]:
        _in[i+1] = '.'
        _in[i+2] = '.'

print(''.join(s for s in _in if s != '.'))
