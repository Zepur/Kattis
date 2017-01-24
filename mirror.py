T = int(input())

for i in range(T):
    R, C = [int(i) for i in input().split()]
    picture = []
    for j in range(R):
        line = ''
        _i = input()
        for k in range(C):
            line += _i[k]
        picture.append(line)
    picture.append(str(i + 1)[::-1] + ' tseT')

    for p in picture[::-1]:
        print(''.join(_p for _p in p[::-1]))
