import math

height, angle = input().split()
h = int(height)
v = math.sin(math.radians(int(angle)))
print(math.ceil(h/v))
