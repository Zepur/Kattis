N = int(input())
target_s = 'Simon says '
x = len(target_s)

for i in range(N):
    s = input()
    if s.startswith(target_s):
        print(s[x:])
