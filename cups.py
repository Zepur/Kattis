import operator

N = int(input())
cups = {}

for i in range(N):
    l = input().split()
    try:
        n = float(l[0]) / 2
        s = l[1]
    except ValueError:
        s = l[0]
        n = float(l[1])
    # print(s)
    cups[s] = n

sorted_x = sorted(cups.items(), key=operator.itemgetter(1))

for x in sorted_x:
    print(str(x[0]))
