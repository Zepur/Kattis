import math

R, C = [int(i) for i in input().split()]
if R == C:
    print('0.000000')
else:
    area_Cheese = math.pi * (R-C)**2
    area_Full = math.pi * R**2
    percentage = round((100 * area_Cheese) / area_Full, 6)
    print(str(percentage))
