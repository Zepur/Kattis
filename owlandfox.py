T = int(input())
l = [1, 10, 100, 1000, 10000, 100000]
ans = []

for i in range(T):
    N = int(input())
    if N in l:
        ans.append('0')
    elif str(N)[-1] == '0':
        x = len(str(N)) - len(str(N).rstrip('0'))
        ans.append(str(N - l[x]))
    else:
        ans.append(str(N - 1))

for s in ans:
    print(s)
