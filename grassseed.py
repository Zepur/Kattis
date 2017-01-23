cost = float(input())
lawns = int(input())
price = 0

for i in range(lawns):
    l, w = [float(x) for x in input().split()]
    price += l*w*cost

print(str(format(price, '.7f')))
