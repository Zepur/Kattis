nums = []

for i in range(3):
    nums.append([int(n) for n in input().split()])
x = []
y = []
for num in nums:
    if num[0] in x:
        x.remove(num[0])
    else:
        x.append(num[0])
    if num[1] in y:
        y.remove(num[1])
    else:
        y.append(num[1])

print(x[0], y[0])
