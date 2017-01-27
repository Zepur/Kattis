X = int(input())
queue = [d for d in input()]
club = ''

it = 0
while len(queue) > 0:
    men = club.count('M')
    women = club.count('W')
    diff = abs(men - women)
    missing = 'W' if men > women else 'M'
    if diff == X:
        if queue[it] == missing:
            club += queue[it]
            queue[it] = '_'
            queue.remove('_')
        elif len(queue) > 1 and queue[it + 1] == missing:
            club += queue[it + 1]
            queue[it + 1] = '_'
            queue.remove('_')
        else:
            break
    elif diff >= 0:
        if queue[it] == missing:
            club += queue[it]
            queue[it] = '_'
            queue.remove('_')
        elif len(queue) > 1 and queue[it + 1] == missing:
            club += queue[it + 1]
            queue[it + 1] = '_'
            queue.remove('_')
        else:
            club += queue[it]
            queue[it] = '_'
            queue.remove('_')

print(str(len(club)))
