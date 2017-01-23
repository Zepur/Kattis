N = int(input())
my_sum = 0

for i in range(N):
    n = input()
    my_sum += int(n[:-1]) ** int(n[-1])

print(str(my_sum))
