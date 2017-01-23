from collections import Counter

N = int(input())

for i in range(N):
    guests = int(input())
    party = [int(g) for g in input().split()]
    odd_man = [k for k, v in Counter(party).items() if v == 1]
    for o in odd_man:
        print('Case #' + str(i + 1) + ': ' + str(o))
