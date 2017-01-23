import sys

consonants = 'bcdfghjklmnpqrstvwxz'
vowels = 'aeiouy'

output = []


def print_res(_line):
        words = [s for s in _line.split()]
        out = ''
        for word in words:
            if word[0] in vowels:
                out += word + 'yay '
            else:
                _i = get_const_idx(word)
                out += word[_i:] + word[:_i] + 'ay '
        return out


def get_const_idx(_w):
    for f in range(len(_w)):
        if _w[f] in vowels:
            return f
    return len(_w) - 1

for i in sys.stdin:
    output.append(print_res(i))
else:
    for l in output:
        print(l)
    quit()
