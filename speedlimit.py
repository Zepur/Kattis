import sys

time = 0
last_time = 0
miles = 0
pr = 0

for inp in sys.stdin:
    if pr == 0:
        pr = int(inp) + 1
    else:
        s = inp
        _m = int(s.split()[0])
        time = int(s.split()[1]) - last_time
        last_time = int(s.split()[1])
        miles += time*_m

    if pr == 1:
        print(str(miles), 'miles')
        time = miles = last_time = 0
    if pr == 0:
        sys.exit()
    pr -= 1
