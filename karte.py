import textwrap

S = input()

GRESKA = 'GRESKA'

cards = textwrap.wrap(S, 3)

for s in cards:
    count_letter = S.count(s)
    if S.count(s) > 1:
        print(GRESKA)
        quit()

count_P = str(13 - S[::3].count('P'))
count_K = str(13 - S[::3].count('K'))
count_H = str(13 - S[::3].count('H'))
count_T = str(13 - S[::3].count('T'))

print(count_P, count_K, count_H, count_T)
