R, C, Zr, Zc = [int(i) for i in input().split()]
lines = []
output = []

for n in range(R):
    line = [c for c in input()]
    lines.append(line)

for l in lines:
    s = ''
    for c in l:
        s += c * Zc
    for n in range(Zr):
        print(s)
