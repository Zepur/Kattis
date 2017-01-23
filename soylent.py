import math

T = int(input())
bottles = []

for i in range(T):
    N = int(input())
    bottles.append(math.ceil(N/400))

for b in bottles:
    print(str(b))
