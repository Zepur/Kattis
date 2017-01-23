s = input()
p = 'PER' * int(len(s)/3)
i = sum(1 for a, b in zip(s, p) if a != b)
print(i)
