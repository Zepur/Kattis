gunnar = [int(n) for n in input().split()]
emma = [int(n) for n in input().split()]
_g1l = gunnar[1] - gunnar[0] + 1
_g2l = gunnar[3] - gunnar[2] + 1
_e1l = emma[1] - emma[0] + 1
_e2l = emma[3] - emma[2] + 1
_g1 = sum(n for n in range(gunnar[0], gunnar[1]+1))
_g2 = sum(n for n in range(gunnar[2], gunnar[3]+1))
_e1 = sum(n for n in range(emma[0], emma[1]+1))
_e2 = sum(n for n in range(emma[2], emma[3]+1))

_sg = (_g1 / _g1l) + (_g2 / _g2l)
_se = (_e1 / _e1l) + (_e2 / _e2l)

print('Tie' if _sg == _se else 'Emma' if _se > _sg else 'Gunnar')
