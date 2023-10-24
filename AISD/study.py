cities = input().split()
d = {city: len(city) for city in cities}
a = sorted(d, key=lambda x: d[x])
print(*a)