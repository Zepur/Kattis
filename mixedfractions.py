while True:
    a, b = [int(i) for i in input().split()]
    if a == b == 0:
        break
    else:
        if a < b:
            print('0 ' + str(a) + ' / ' + str(b))
        else:
            print(str(int(a/b)) + ' ' + str(a % b) + ' / ' + str(b))
