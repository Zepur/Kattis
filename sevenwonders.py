cards = input()
points = 0
occ = {'T': 0, 'C': 0, 'G': 0}

for c in occ.keys():
    points += cards.count(c) ** 2
    occ[c] = cards.count(c)

num = occ.get(min(occ, key=lambda k: occ[k]))
points += 7 * num

print(points)
