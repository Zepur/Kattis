steps = [int(i) for i in input().split()]
steps.sort()

print(str(steps[0] * steps[2]))
