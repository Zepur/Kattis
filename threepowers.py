for i in range(0, 100):
    _in = int(input())
    if _in == 0:
        break
    else:
        _bin = bin(_in - 1)[2:][::-1]
        solution = '{ '
        for b in range(len(_bin)):
            if _bin[int(b)] == '1':
                solution += str(3**b) + ', '
        if len(solution) > 2:
            solution = solution[:-2] + ' }'
        else:
            solution += '}'
    print(solution)
