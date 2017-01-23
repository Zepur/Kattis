import sys
from math import pi

for i in sys.stdin:
    _r, _m, _c = i.split()
    if _r == _m == _c == '0':
        sys.exit()
    r = float(_r)
    m = int(_m)
    c = int(_c)
    area = str(pi * r**2)
    square = r**2 * 2**2
    relative = str((c / m) * square)
    print(area, relative)
