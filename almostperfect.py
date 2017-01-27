import sys
import math


def get_div_sum(numb):
    div_sum = 0
    sq = math.sqrt(numb)
    for i in range(1, math.ceil(math.sqrt(numb))):
        if i == sq:
            break
        if i > numb / i:
            return div_sum
        if numb % i == 0:
            div_sum += i
            if i != 1:
                div_sum += (numb / i)
    if sq * sq == numb:
        if sq == int(sq):
            div_sum += int(sq)
    return div_sum


ans = []
for line in sys.stdin:
        d = int(line)
        divs = get_div_sum(d)
        ans.append((d, divs))
else:
    for s in ans:
        if abs(s[1] - s[0]) == 0:
            print(s[0], 'perfect')
        elif abs(s[1] - s[0]) > 2:
            print(s[0], 'not perfect')
        else:
            print(s[0], 'almost perfect')
