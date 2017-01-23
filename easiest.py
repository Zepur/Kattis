def solve(i):
    sum_i = sum(int(x) for x in str(i))
    _x = 0
    p = 11
    while _x != sum_i:
        _p = p * i
        sum_p = sum(int(x) for x in str(_p))
        if sum_p == sum_i:
            return p
        p += 1


while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
