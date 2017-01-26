import math

ds = []

while True:
    D, V = [int(i) for i in input().split()]
    if D == V == 0:
        break
    tot_VOL = (2 * math.pi * (D / 2) * D) + (2 * math.pi * (D / 2) ** 2)
    d = (D*D*D - (6*V / math.pi)) ** (1.0/3)
    ds.append(d)

for _d in ds:
    print(_d)
