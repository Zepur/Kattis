import sys

got_int = False
lines_read = 0


def solvis(n):
    global got_int, lines_read
    if not got_int:
        lines_read = int(n.split()[0])
        print(int(n.split()[1]))
        got_int = True
    else:
        lines_read -= 1
    if lines_read == 0:
        got_int = False


for i in sys.stdin:
    solvis(i)
