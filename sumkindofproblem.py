P = int(input())

for i in range(P):
    s = input()
    _k, _n = (int(_i) for _i in s.split())
    x = 1 if _n % 2 == 0 else 0
    s1 = int((0.5 * _n)*(_n+1))
    s2 = _n**2
    s3 = _n*(_n+1)
    print(str(_k) + ' ' + str(s1) + ' ' + str(s2) + ' ' + str(s3))
