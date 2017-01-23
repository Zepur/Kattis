import sys

nums = 0
modulos = []


def solve(n):
    global nums
    nums += 1
    m = int(n) % 42
    if m not in modulos:
        modulos.append(m)
    if nums == 10:
        print(len(modulos))
        nums = 0
        modulos.clear()


for i in sys.stdin:
    solve(i)
