runs = 1
while True:
    n = int(input())
    if n == 0:
        quit()
    names = []
    for i in range(n):
        names.append(input())
    output = list(names[::2])
    if n % 2 == 0:
        for s in names[-1::-2]:
            output.append(s)
    else:
        for s in names[-2::-2]:
            output.append(s)
    print('SET ' + str(runs))
    for o in output:
        print(o)
    runs += 1
