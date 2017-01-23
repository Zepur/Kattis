N = input()
n = input()
print(sum(1 for i in [int(b) for b in n.split()] if i < 0))
