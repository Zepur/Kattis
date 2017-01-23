T = int(input())
cities = set()
trips = 0

while trips < T:
    x = input()
    if len(x) == 0:
        break
    n = int(x)
    for i in range(n):
        s = input()
        cities.add(s)
    print(str(len(cities)))
    trips += 1
    cities = set()
