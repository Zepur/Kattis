import string
import random
from math import ceil

import time

a, b = input().split()

start_time = int(round(time.time() * 1000))

A = int(a)
B = int(b)
letters = string.ascii_lowercase[:26]
_i = max(A, ceil(B/2))
words = list()
unique_words = set()


def r_w():
    s = ''
    while len(s) < 7:
        c = letters[random.randint(0, 25)]
        s += c
    if s in unique_words:
        return r_w()
    else:
        return s


while len(words) < _i:
    if len(unique_words) == ceil(B/2):
        words.extend(unique_words)
        d = _i - len(words)
        _d = [words[0]] * d
        words.extend(_d)
    else:
        unique_words.add(r_w())

print(' '.join(x for x in words))

end_time = int(round(time.time() * 1000))
print(str(end_time - start_time))
