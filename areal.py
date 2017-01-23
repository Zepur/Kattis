import math

n = float(input())
s = math.sqrt(n)
if s == int(s):
    print(int(s*4))
else:
    print(s*4)
