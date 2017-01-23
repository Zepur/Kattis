import datetime

current = input().replace(':', '')
explosion = input().replace(':', '')
if current == explosion:
    print('24:00:00')
    exit()
_start = datetime.datetime.strptime(current, '%H%M%S')
_end = datetime.datetime.strptime(explosion, '%H%M%S')
_time = str((_end - _start))
_explosion = _time[-8:]
if _explosion[0] == ' ':
    _explosion = '0' + _explosion[1:]
elif len(_explosion) < 8:
    _explosion = '0' + _explosion
print(_explosion)

