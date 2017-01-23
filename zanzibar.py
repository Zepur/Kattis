T = int(input())
tot_turts = []

for i in range(T):
    _turts = 0
    turts = [int(y) for y in input().split()]
    for _t in range(len(turts)-2):
        if 2*turts[_t] < turts[_t + 1]:
            _turts += turts[(_t + 1)] - (2 * turts[_t])
    tot_turts.append(_turts)

for t in tot_turts:
    print(str(t))
