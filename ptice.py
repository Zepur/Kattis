N = int(input())
correct = input()
Adrian = 'ABC'
Bruno = 'BABC'
Goran = 'CCAABB'
if N > 3:
    Adrian = ('ABC' * (N - len('ABC')+1))[:N]
if N > 4:
    Bruno = ('BABC' * (N - len('BABC')+1))[:N]
if N > 6:
    Goran = ('CCAABB' * (N - len('CCAABB')+1))[:N]

winners = []

a = sum([1 for i, x in enumerate(correct) if x == Adrian[i]])
score = a
winners.append('Adrian')
b = sum([1 for i, x in enumerate(correct) if x == Bruno[i]])
if b > score:
    score = b
    winners.clear()
    winners.append('Bruno')
elif b == score:
    winners.append('Bruno')
c = sum([1 for i, x in enumerate(correct) if x == Goran[i]])
if c > score:
    score = c
    winners.clear()
    winners.append('Goran')
elif c == score:
    winners.append('Goran')

print(score)
for w in winners:
    print(w)
