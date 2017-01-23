R, C = input().split()
_map = []

for i in range(int(R)):
    _map.append([s for it, s in enumerate(input()) if it < int(C)])

pos = (0, 0)
moves = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
num_moves = 0
result = ''
x_oob = [-1, int(R)]
y_oob = [-1, int(C)]

while True:
    new_pos = (pos[0], pos[1])
    if pos[0] in x_oob or pos[1] in y_oob:
        result += 'Out'
        break
    elif _map[pos[0]][pos[1]] == 'T':
        result += str(num_moves)
        break
    elif _map[pos[0]][pos[1]] == 'X':
        result += 'Lost'
        break
    elif _map[pos[0]][pos[1]] in moves:
        pos = tuple(map(sum, zip(new_pos, moves.get(_map[pos[0]][pos[1]]))))
        num_moves += 1
        _map[new_pos[0]][new_pos[1]] = 'X'

print(result)
