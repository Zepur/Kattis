N = int(input())

for i in range(N):
    r, s = input().split()
    for j in range(int(r)):
        q = int(len(s) / 4)
        if q == 0:
            break
        if j % 2 != 0:
            s = s[0:len(s)-q]
        else:
            s = s[q:]

    print(s)
