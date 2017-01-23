first = input().split()
N = int(first[0])
B = first[1]
cards = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
cards_dom = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
points = 0

for i in range(4*N):
    _in = input()
    points += cards_dom.get(_in[0]) if _in[1] == B else cards.get(_in[0])

print(points)
