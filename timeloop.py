import sys


def loop(i):
    for n in range(1, int(i)+1):
        print(str(n) + ' Abracadabra')

for x in sys.stdin:
    loop(x)
