numbers = [1, 6, 14, 96, 87, 99]

a = list(filter(lambda x: x%2 == 0, numbers))
print(*a, sep=', ')